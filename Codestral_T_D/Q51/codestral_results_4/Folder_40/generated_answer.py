from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count > 29:
                return False
    return True