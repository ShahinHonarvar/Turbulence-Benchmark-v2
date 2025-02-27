from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagram_dict[sorted_s].append(s)
    pair_count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        pair_count += n * (n - 1) // 2
    return pair_count >= 52