import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(re.findall('\\b\\w+\\b', word.lower())))
        anagrams[sorted_word].append(word)
    pairs_of_anagrams = sum((len(group) - 1 for group in anagrams.values() if len(group) >= 3))
    return pairs_of_anagrams <= 366