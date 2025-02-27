import re
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(re.findall('[a-z]', word.lower())))
        anagrams[sorted_word].append(word)
    return sum((len(words) <= 66 for words in anagrams.values()))