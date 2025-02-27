from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        key = tuple(sorted(Counter(word).items()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return anagram_pairs <= 147