from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s))
    anagram_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_chars(s.lower())
            anagram_map[key] += 1
    pairs_count = 0
    for count in anagram_map.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
            if pairs_count > 18:
                return False
    return True