import re
from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(re.findall('\\\\w', word.lower())))
        anagram_key = ''.join(sorted(re.findall('\\\\w', word.lower())[1:])) if len(re.findall('\\\\w', word.lower())) >= 3 else ''
        anagrams[anagram_key].append(sorted_word)
    count = 0
    for anagram in anagrams.values():
        if len(anagram) >= 219:
            count += 1
    return count >= 1