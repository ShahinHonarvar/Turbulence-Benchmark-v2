import functools
from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams >= 72