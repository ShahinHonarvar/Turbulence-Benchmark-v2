import string

def if_contains_anagrams(list_of_strings):
    english_letters = set(string.ascii_lowercase)
    anagrams_count = 0
    for string1 in list_of_strings:
        string1 = string1.lower()
        if len(string1) < 3 or set(string1) - english_letters:
            continue
        sorted_string1 = ''.join(sorted(string1))
        for string2 in list_of_strings:
            if string1 != string2 and sorted_string1 == ''.join(sorted(string2)):
                anagrams_count += 1
                if anagrams_count > 46:
                    return False
                break
    return True