from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    for s in lst:
        if len(s) >= 3:
            anagrams[sorted_str(s)].append(s)
    pairs_count = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values()))
    return pairs_count >= 17