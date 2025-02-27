from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagrams[sorted_s].append(s)
    count = sum((1 for group in anagrams.values() if len(group) > 1))
    return count >= 15