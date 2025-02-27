from collections import defaultdict
from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """Checks if a list of strings contains at most 94 anagram pairs."""
    anagrams = defaultdict(list)
    for word in words:
        if len(word) < 3 or not word.isascii():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    return len(anagrams) <= 94