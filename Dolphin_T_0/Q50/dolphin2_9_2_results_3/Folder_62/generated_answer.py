from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = 0
    for key in c:
        n = c[key]
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 43