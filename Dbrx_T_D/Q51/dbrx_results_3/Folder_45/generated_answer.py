import string

def if_contains_anagrams(list_of_strings):
    english_letters = set(string.ascii_lowercase)
    anagrams = set()
    for word in list_of_strings:
        word = word.lower()
        if len(word) < 3 or not set(word).issubset(english_letters):
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            return True
        anagrams.add(sorted_word)
    return len(anagrams) > 464