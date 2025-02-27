from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) < 3:
            continue
        counter[tuple(sorted(word.lower()))] += 1
    counter = [v for v in counter.values() if v >= 2]
    return len(counter) >= 79