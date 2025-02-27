from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            d[key].append(word)
    return sum((len(val) > 1 for val in d.values())) <= 4