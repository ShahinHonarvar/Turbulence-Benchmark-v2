from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            pairs += len(group) * (len(group) - 1) // 2
            if pairs > 445:
                return False
    return pairs <= 445