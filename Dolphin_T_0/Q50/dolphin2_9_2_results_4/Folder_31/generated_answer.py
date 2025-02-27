from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    count = 0
    for word in lst:
        if len(word) >= 3 and word.islower():
            c[tuple(sorted(word))] += 1
    for key in c:
        if c[key] > 1:
            count += c[key] * (c[key] - 1) // 2
    return count >= 68