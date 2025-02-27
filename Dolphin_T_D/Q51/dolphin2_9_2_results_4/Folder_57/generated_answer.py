from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            count[tuple(sorted(word))] += 1
    pairs = 0
    for value in count.values():
        pairs += value // 2
        if pairs > 74:
            break
    return pairs <= 74