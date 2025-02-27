import re
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams.append(sorted_word)
    anagrams_count = Counter(anagrams)
    if max(anagrams_count.values()) > 210:
        return False
    return True