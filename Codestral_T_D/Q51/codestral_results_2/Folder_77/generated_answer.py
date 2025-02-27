from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        key = tuple(sorted(Counter(lower_word).items()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 17