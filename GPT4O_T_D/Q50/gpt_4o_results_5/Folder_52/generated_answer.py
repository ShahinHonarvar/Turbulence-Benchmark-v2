from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_map[sorted_str(s)] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return pairs_count >= 58