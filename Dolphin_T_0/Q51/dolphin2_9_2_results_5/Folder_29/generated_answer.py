from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for string in list_of_strings:
        counter[tuple(sorted(string.lower()))] += 1
    return sum((n * (n - 1) // 2 <= 318 for n in counter.values() if len(n) >= 3))