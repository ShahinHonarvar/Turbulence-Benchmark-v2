import re

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    total_anagrams = sum(anagrams.values()) // 2
    return total_anagrams >= 194