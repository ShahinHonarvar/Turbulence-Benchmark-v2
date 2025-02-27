import re
from collections import Counter

def if_contains_anagrams(words):
    anagrams = []
    for word in words:
        sorted_word = ''.join(sorted(re.findall('\\b\\w{3,}\\b', word.lower())))
        if sorted_word:
            anagrams.append(sorted_word)
    anagram_counts = Counter(anagrams)
    return max(anagram_counts.values()) <= 366