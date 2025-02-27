from collections import Counter

def if_contains_anagrams(arr):
    c = Counter()
    for word in arr:
        if len(word) >= 3:
            word = word.lower()
            c.update(Counter(word))
    pairs = 0
    for v in c.values():
        if v & v - 1 < 1:
            pairs += bin(v).count('1') - 1
    return pairs <= 66