import string

def if_contains_anagrams(string_list):
    anagram_count = 0
    english_letters = set(string.ascii_lowercase)
    for string1 in string_list:
        string1 = string1.lower()
        if len(string1) < 3:
            continue
        string_set = set(string1)
        if len(string_set & english_letters) < 3:
            continue
        for string2 in string_list:
            string2 = string2.lower()
            if string1 == string2 or len(string2) < 3:
                continue
            if set(string2) & english_letters < 3:
                continue
            if sorted(string1) == sorted(string2):
                anagram_count += 1
                if anagram_count > 94:
                    return False
    return True