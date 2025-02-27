from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagrams = defaultdict(list)
    for s in strings:
        anagrams[''.join(sorted(s))].append(s)
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 39:
            return False
    return True