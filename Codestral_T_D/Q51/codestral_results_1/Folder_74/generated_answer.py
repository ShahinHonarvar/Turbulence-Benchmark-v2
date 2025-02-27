from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    return sum((x * (x - 1) // 2 for x in counter.values())) <= 57