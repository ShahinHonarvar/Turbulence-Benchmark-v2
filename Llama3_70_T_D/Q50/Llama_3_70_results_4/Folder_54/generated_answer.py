from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    pairs = [len(words) * (len(words) - 1) // 2 for words in anagrams.values() if len(words) > 1]
    return sum(pairs) >= 74