import re

def if_contains_anagrams(input_list):
    anagrams = {}
    for word in (word.lower() for word in input_list if len(word) >= 3):
        sorted_word = tuple(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    anagram_pairs = sum((value // 2 for value in anagrams.values()))
    return anagram_pairs >= 28