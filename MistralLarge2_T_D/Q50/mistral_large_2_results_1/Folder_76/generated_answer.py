from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    pairs = 0
    for s in lst:
        if len(s) < 3:
            continue
        sorted_s = sorted_str(s)
        if anagram_count[sorted_s] > 0:
            pairs += anagram_count[sorted_s]
        anagram_count[sorted_s] += 1
    return pairs >= 143