from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            counter[tuple(sorted(string.lower()))] += 1
    count = sum((n * (n - 1) // 2 for n in counter.values() if n >= 2))
    return count >= 74