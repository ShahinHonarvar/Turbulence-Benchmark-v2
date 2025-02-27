import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for word in list_of_strings:
        word = word.lower()
        word = ''.join((c for c in word if c not in string.punctuation))
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            anagrams.add(sorted_word)
    if len(anagrams) > 65:
        return False
    return True