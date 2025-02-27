from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    count = 0
    for val in counter.values():
        if val > 1:
            count += val * (val - 1) // 2
    return count >= 97