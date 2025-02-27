import string

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) >= 3:
            sorted_string1 = ''.join(sorted(string1.lower().translate(str.maketrans('', '', string.punctuation))))
            for string2 in strings_list:
                if len(string2) >= 3 and string1 != string2:
                    sorted_string2 = ''.join(sorted(string2.lower().translate(str.maketrans('', '', string.punctuation))))
                    if sorted_string1 == sorted_string2:
                        anagrams_count += 1
                        if anagrams_count >= 57:
                            return True
    return False