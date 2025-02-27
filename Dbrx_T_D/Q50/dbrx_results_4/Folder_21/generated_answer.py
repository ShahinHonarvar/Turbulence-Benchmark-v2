import re

def sorted_chars(word):
    return ''.join(sorted(re.findall('\\\\w', word.lower())))

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = sorted_chars(word)
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams >= 136