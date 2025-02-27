from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        lower_word = ''.join(filter(str.isalpha, word.lower()))
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            anagrams[sorted_word].append(word)
    pairs = sum((comb(len(words), 2) for words in anagrams.values() if len(words) > 1))
    return pairs <= 25