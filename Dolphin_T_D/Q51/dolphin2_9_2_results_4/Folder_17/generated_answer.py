from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        if len(word) >= 3:
            w = word.lower()
            c[tuple(sorted(w))] += 1
    count = 0
    for key, value in c.items():
        n = value
        while n > 1:
            n //= 2
            count += n
    if count > 22:
        return True
    else:
        return False