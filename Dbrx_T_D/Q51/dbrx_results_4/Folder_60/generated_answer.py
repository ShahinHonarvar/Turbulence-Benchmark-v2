import string

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    english_letters = set(string.ascii_lowercase)
    for word in list_of_strings:
        word = word.lower()
        if len(word) < 3 or len(set(word)) == len(word):
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in english_letters:
            anagrams_count += 1
            english_letters.remove(sorted_word)
        if anagrams_count > 77:
            return False
    return True