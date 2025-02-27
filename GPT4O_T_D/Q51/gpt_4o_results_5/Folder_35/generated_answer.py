from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize_string(s)
            anagram_dict[normalized].append(s)
    pair_count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            pair_count += n * (n - 1) // 2
        if pair_count > 210:
            return False
    return True