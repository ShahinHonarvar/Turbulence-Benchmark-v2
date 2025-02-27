import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            anagrams.add(sorted_word)
    return len(anagrams) <= 65