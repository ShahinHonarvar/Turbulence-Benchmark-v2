from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for word in list_of_strings:
        if len(word) >= 3:
            for other_word in list_of_strings:
                if other_word != word:
                    if Counter(word.lower()) == Counter(other_word.lower()):
                        count += 1
    if count <= 28:
        return True
    else:
        return False