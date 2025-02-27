from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 42:
                return True
    return False