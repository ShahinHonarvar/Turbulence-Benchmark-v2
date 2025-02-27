from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            anagram_map[sorted_s] += 1
    pair_count = 0
    for count in anagram_map.values():
        pair_count += count * (count - 1) // 2
    return pair_count >= 17