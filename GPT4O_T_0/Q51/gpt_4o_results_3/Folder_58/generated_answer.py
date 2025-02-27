from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 60:
                return False
    return True