from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_count[sorted_s] += 1
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 61