import string

def if_contains_anagrams(string_list):
    anagrams = {}
    english_letters = string.ascii_lowercase
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3 and sorted_word in anagrams and (anagrams[sorted_word] < 44):
            anagrams[sorted_word] += 1
        elif len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams[sorted_word] = 1
    return max(anagrams.values()) < 44