from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    count = 0
    pairs = 0
    for key, value in counter.items():
        if value >= 2:
            count += 1
            pairs += value * (value - 1) // 2
    return pairs >= 10