from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for s in strings:
        sorted_s = sorted_string(s)
        if len(sorted_s) >= 3:
            anagram_map[sorted_s].append(s)
    anagram_pairs_count = 0
    for key in anagram_map:
        group_length = len(anagram_map[key])
        if group_length > 1:
            anagram_pairs_count += group_length * (group_length - 1) // 2
    return anagram_pairs_count >= 70