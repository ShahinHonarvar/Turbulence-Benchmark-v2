from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    pair_count = 0
    for key in anagrams:
        n = len(anagrams[key])
        pair_count += n * (n - 1) // 2
    return pair_count <= 41