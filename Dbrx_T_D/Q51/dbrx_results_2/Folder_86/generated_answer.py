import string

def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word not in anagrams:
            anagrams.add(sorted_word)
    return len(anagrams) <= 48