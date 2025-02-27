from collections import Counter

def if_contains_anagrams(s):
    counts = {}
    for word in s:
        word = word.lower()
        if len(word) < 3:
            continue
        c = Counter(word)
        key = ''.join(sorted(c.elements()))
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    length = len(counts)
    return length <= 20