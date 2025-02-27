from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized_s = normalize(s)
            anagram_map[normalized_s] += 1
    pairs = 0
    for count in anagram_map.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 74:
                return False
    return True