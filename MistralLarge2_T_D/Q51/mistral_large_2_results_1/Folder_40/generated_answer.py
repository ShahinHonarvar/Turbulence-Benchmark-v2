from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagrams[sorted_str].append(s)
    count = sum((len(group) > 1 for group in anagrams.values()))
    return count <= 29