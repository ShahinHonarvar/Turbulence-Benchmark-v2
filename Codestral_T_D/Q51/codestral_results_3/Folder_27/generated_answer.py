from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = tuple(sorted(Counter(word).items()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return sum((n * (n - 1) // 2 for n in anagrams.values())) <= 113