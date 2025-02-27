from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            d[key].append(word)
    for key in d:
        if len(d[key]) >= 2:
            return True
    return False