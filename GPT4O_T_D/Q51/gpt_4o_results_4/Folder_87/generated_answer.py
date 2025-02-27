from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str] += 1
    count = 0
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 392:
            return False
    return True