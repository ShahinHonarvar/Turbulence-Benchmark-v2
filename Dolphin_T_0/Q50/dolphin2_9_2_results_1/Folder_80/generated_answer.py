from collections import Counter

def if_contains_anagrams(lst):
    anagrams = 0
    for word in lst:
        if len(word) >= 3:
            for other_word in lst:
                if word != other_word and Counter(word.lower()) == Counter(other_word.lower()):
                    anagrams += 1
    return anagrams >= 19