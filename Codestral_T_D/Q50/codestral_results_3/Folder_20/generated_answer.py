from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[frozenset(Counter(word.lower()))] += 1
    return sum((value * (value - 1) // 2 for value in counter.values())) >= 64