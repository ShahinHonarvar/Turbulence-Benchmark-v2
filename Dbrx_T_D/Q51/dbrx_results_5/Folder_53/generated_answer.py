import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(re.findall('[a-zA-Z]{3,}', word.lower())))
        anagrams[sorted_word].append(word)
    anagram_pairs = [len(group) for group in anagrams.values() if len(group) > 1]
    return sum(anagram_pairs) <= 8