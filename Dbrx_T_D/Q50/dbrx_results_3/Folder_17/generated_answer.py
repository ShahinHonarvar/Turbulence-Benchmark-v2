from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) < 3:
            continue
        for string2 in strings_list:
            if len(string2) < 3 or string1 == string2:
                continue
            if Counter(string1.lower()) == Counter(string2.lower()):
                anagrams_count += 1
                if anagrams_count >= 97:
                    return True
    return False