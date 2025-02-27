from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    strings = [s.lower() for s in strings]
    potential_anagrams = [s for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for string in potential_anagrams:
        sorted_str = ''.join(sorted(string))
        anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for values in anagram_dict.values():
        n = len(values)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs >= 77:
                return True
    return anagram_pairs >= 77