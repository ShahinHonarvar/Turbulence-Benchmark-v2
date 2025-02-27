import string

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_letters for c in sorted_word)):
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
    return sum((len(words) - 1 for words in anagrams.values())) <= 18