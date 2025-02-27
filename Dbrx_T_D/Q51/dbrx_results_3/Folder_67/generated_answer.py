import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            anagram_pairs += 1
            if anagram_pairs > 5:
                return False
    return True if anagram_pairs <= 5 else False