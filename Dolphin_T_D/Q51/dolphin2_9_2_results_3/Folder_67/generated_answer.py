from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        word = word.replace(' ', '').lower()
        if len(word) >= 3:
            c.update(Counter(word))
    pairs_count = 0
    for key in c:
        if c[key] > 1:
            pairs_count += 1
            c[key] = 1
    return pairs_count <= 5