import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(re.findall('[a-z]', word.lower())))
        anagrams[sorted_word].append(word)
    return sum((len(anagrams[word]) >= 2 for word in anagrams)) <= 16