from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            counter[tuple(sorted(string))] += 1
    pairs = sum((v * (v - 1) // 2 for v in counter.values() if v >= 2))
    return pairs <= 64