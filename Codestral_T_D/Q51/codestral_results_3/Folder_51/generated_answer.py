from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counter[frozenset(Counter(word).items())] += 1
    for val in counter.values():
        count += val * (val - 1) // 2
    return count <= 116