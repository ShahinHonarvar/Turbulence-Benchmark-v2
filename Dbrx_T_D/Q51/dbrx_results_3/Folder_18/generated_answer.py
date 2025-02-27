import string

def if_contains_anagrams(strings):
    anagrams = []
    english_letters = set(string.ascii_lowercase)
    for word in strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if all((letter in english_letters for letter in sorted_word)):
            anagrams.append(sorted_word)
    return len(set(anagrams)) <= 42