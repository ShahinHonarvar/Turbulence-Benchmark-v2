from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        anagrams[''.join(sorted(s_lower))].append(s_lower)
    count = 0
    for v in anagrams.values():
        if len(v) > 1 and len(v[0]) >= 3:
            count += len(v) * (len(v) - 1) // 2
    return count >= 58