import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = tuple(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pairs <= 147