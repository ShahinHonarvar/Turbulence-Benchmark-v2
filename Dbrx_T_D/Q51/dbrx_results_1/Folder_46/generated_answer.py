import string

def if_contains_anagrams(words):
    anagrams = set()
    for word in words:
        word = word.lower()
        if len(word) < 3 or not word.isalpha():
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            return True
        anagrams.add(sorted_word)
    return len(anagrams) <= 61