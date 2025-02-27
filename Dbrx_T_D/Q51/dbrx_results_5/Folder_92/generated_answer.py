import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in anagrams:
            return True
        anagrams.add(sorted_word)
    return len(anagrams) > 34