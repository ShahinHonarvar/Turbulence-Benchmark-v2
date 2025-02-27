import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    return sum(anagrams.values()) <= 36