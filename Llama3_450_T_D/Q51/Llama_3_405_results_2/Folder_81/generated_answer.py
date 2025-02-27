from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    count = sum((len(values) * (len(values) - 1) // 2 for values in anagrams.values()))
    return count <= 79