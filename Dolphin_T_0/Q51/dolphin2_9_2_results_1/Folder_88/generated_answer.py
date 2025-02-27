from collections import Counter

def if_contains_anagrams(lst):
    c = 0
    d = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            counter = Counter(word)
            key = ''.join(sorted(counter.keys()))
            if key not in d:
                d[key] = [word]
            else:
                d[key].append(word)
    for key in d:
        if len(d[key]) > 1:
            pairs = len(d[key]) * (len(d[key]) - 1) // 2
            c += pairs
    if c > 407:
        return False
    else:
        return True