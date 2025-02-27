import string

def if_contains_anagrams(list_of_strings):
    english_letters = set(string.ascii_lowercase)
    anagrams = {}
    for word in list_of_strings:
        word = word.lower()
        if len(word) < 3 or not set(word) <= english_letters:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
            if anagrams[sorted_word] > 1:
                return True
        else:
            anagrams[sorted_word] = 1
    return False