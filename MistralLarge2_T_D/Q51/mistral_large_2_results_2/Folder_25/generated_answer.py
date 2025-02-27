from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    counts = defaultdict(int)
    pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        counts[sorted_s] += 1
        if counts[sorted_s] > 1:
            pairs += counts[sorted_s] - 1
    return pairs <= 67