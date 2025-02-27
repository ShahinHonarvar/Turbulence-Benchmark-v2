from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = tuple(sorted(Counter(word).items()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    pair_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pair_count <= 98