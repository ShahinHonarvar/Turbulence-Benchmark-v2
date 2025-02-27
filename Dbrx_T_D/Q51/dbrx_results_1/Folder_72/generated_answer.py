import string

def if_contains_anagrams(strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for word in strings:
        if len(word) < 3 or not word.isalpha():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams.add(sorted_word)
        else:
            return True
    return len(anagrams) <= 188