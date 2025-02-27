from collections import Counter

def if_contains_anagrams(lst):
    anagrams = Counter()
    for word in lst:
        if len(word) >= 3:
            anagrams[tuple(sorted(word.lower()))] += 1
    return sum((val * (val - 1) // 2 for val in anagrams.values())) >= 60