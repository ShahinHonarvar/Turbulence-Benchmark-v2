from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = defaultdict(int)
    pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        count[sorted_s] += 1
    for v in count.values():
        if v >= 2:
            pairs += v * (v - 1) // 2
    return pairs >= 115