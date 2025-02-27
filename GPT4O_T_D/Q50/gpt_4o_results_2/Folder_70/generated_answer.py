from collections import defaultdict

def if_contains_anagrams(lst):

    def normalized(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_map[normalized(word)] += 1
    pair_count = 0
    for count in anagram_map.values():
        pair_count += count * (count - 1) // 2
        if pair_count >= 189:
            return True
    return False