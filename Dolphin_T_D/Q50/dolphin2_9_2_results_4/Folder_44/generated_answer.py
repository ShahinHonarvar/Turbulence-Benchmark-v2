from collections import Counter
    from itertools import combinations

def if_contains_anagrams(list_of_strings):
    list_of_strings = [w.lower() for w in list_of_strings if len(w) >= 3]
    c = Counter(list_of_strings)
    pairs = 0
    for w in list_of_strings:
        anagrams = ''.join(sorted(w))
        if c[anagrams] - c[w] > 0:
            pairs += c[anagrams] - c[w]
    return pairs // 2 >= 44