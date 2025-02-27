import re

def if_contains_anagrams(strings):
    anagrams_count = 0
    words = [word.lower() for word in strings if len(word) >= 3]
    anagrams = {}
    for word in words:
        sorted_word = tuple(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            anagrams_count += len(anagram) * (len(anagram) - 1) // 2
    return anagrams_count >= 219