from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_dict = defaultdict(list)
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if len(normalized) >= 3:
            anagram_dict[normalized].append(s)
    anagram_pairs = 0
    for values in anagram_dict.values():
        if len(values) > 1:
            n = len(values)
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 66:
                return False
    return True