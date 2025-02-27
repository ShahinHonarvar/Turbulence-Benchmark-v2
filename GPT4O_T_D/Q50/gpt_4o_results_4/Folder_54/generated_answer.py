from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[normalize_string(s)].append(s)
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n >= 2:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs >= 74:
            return True
    return False