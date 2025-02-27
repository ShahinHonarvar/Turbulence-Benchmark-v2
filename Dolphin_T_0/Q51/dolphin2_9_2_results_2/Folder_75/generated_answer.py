from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        clean_word = ''.join(Counter(word.lower()).elements())
        if len(clean_word) >= 3:
            if clean_word in anagrams:
                anagrams[clean_word] += 1
            else:
                anagrams[clean_word] = 1
    pairs = 0
    for key in anagrams:
        pairs += anagrams[key] * (anagrams[key] - 1) // 2
    return pairs <= 55