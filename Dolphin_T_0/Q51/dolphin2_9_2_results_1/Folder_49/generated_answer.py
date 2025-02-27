from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        c = Counter(word.lower())
        key = ''.join(sorted(c.keys()))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(c)
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            pairs = len(anagrams[key]) // 2
            count += pairs
    return count <= 10