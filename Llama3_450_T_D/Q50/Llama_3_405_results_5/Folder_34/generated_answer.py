from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 25