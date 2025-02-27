import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = tuple(sorted(re.findall('[a-zA-Z]{3,}', word.lower())))
        anagrams[sorted_word].append(word)
    anagram_pairs = sum((1 for w in anagrams.values() if len(w) > 1))
    return anagram_pairs <= 401