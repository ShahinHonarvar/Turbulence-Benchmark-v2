import re
from collections import Counter

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    count = 0
    for value in anagrams.values():
        if len(value) > 1 and len(value) * (len(value) - 1) // 2 >= 30:
            return True
    return False