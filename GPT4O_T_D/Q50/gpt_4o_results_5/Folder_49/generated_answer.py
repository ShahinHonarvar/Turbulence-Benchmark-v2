from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagrams[sorted_str] += 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values() if v > 1))
    return count >= 59