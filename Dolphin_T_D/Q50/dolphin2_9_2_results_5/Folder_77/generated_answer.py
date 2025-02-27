from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        counter[tuple(sorted(word.lower()))] += 1
    pairs = 0
    for count in counter.values():
        pairs += count * (count - 1) // 2
    return pairs >= 209