from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    return sum((n * (n - 1) // 2 for n in counter.values())) >= 188