import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for word in list_of_strings:
        word = word.lower()
        sorted_word = ''.join(sorted(filter(english_letters.__contains__, word)))
        if len(sorted_word) >= 3:
            anagrams.add(sorted_word)
    return len(anagrams) <= 47