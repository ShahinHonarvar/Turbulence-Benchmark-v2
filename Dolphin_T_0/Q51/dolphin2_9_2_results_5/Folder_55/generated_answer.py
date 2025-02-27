from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counter[tuple(sorted(word))] += 1
    pairs = 0
    for key in counter:
        pairs += counter[key] * (counter[key] - 1) // 2
        count += 1
    return False if count <= 44 and pairs > 0 else True