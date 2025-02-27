from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) < 3:
            continue
        normalized = normalize(s)
        anagrams[normalized].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count >= 57