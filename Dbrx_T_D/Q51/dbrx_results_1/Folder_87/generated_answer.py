import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = tuple(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
    pairs = sum((count // 2 for count in anagrams.values() if count >= 2))
    return pairs <= 392