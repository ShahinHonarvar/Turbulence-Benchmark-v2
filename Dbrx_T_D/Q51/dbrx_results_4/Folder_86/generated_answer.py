import string

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower().replace(' ', '')))
        for string2 in strings_list:
            if string1 == string2:
                continue
            if len(string2) < 3:
                continue
            sorted_string2 = ''.join(sorted(string2.lower().replace(' ', '')))
            if sorted_string1 == sorted_string2:
                anagrams_count += 1
                if anagrams_count > 47:
                    return True
    return False