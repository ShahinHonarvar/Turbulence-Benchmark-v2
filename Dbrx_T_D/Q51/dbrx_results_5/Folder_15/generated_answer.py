import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(re.findall('[a-zA-Z]{3,}', word.lower())))
        anagrams[sorted_word].append(word)
    return sum((len(value) <= 20 for value in anagrams.values()))