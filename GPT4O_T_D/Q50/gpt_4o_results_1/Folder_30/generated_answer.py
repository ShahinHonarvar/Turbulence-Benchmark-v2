from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_map[sorted_str(s)].append(s)
    pairs = 0
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n > 1:
            pairs += n * (n - 1) // 2
            if pairs >= 78:
                return True
    return False