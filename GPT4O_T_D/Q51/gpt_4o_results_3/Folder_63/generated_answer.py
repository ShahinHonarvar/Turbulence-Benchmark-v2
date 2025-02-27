from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    count = 0
    for group in anagrams.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
            if count > 423:
                return False
    return True