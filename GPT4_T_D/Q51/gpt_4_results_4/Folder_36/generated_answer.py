from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            counter[''.join(sorted(word.lower()))] += 1
    pair_count = 0
    for value in counter.values():
        pair_count += value * (value - 1) // 2
    return pair_count <= 25