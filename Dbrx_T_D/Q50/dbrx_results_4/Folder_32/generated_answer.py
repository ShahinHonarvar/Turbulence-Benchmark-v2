import functools
from collections import Counter

def sort_string(string):
    return ''.join(sorted(string))

def is_anagram(string1, string2):
    return sort_string(string1) == sort_string(string2)

def anagram_pairs(word_list):
    anagrams = {}
    pairs = 0
    for word in word_list:
        sorted_word = tuple(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
            pairs += anagrams[sorted_word] - 1
        else:
            anagrams[sorted_word] = 1
    return pairs

def if_contains_anagrams(word_list):
    min_length = 3
    word_list = [word.lower() for word in word_list if len(word) >= min_length]
    return anagram_pairs(word_list) >= 194