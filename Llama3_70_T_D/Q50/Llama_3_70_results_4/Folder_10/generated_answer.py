from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for words in anagrams.values():
        if len(words) >= 2:
            count += comb(len(words), 2)
    return count >= 52