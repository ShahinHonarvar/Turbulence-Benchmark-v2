from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            c[word] += 1
    count = sum((v * (v - 1) // 2 for v in c.values() if v >= 2))
    return count <= 38