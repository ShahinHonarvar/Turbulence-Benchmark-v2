from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                if Counter(string1.lower()) == Counter(string2.lower()):
                    count += 1
    if count > 94:
        return False
    else:
        return True