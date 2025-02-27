from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    result = False
    for word in lst:
        if len(word) >= 3:
            c[tuple(sorted(word.lower()))] += 1
    count = 0
    for key in c.keys():
        if c[key] > 1:
            count += 1
            if count >= 6:
                return True
    return False