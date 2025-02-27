import string

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) >= 3:
            for string2 in strings_list:
                if string1 != string2 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                    anagrams_count += 1
    return anagrams_count >= 276