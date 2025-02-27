from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        word = ''.join(sorted(word.lower()))
        c[word] += 1
    return any((x >= 2 for x in c.values() if len(x) > 2)) and len(c) <= 40