import string

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) >= 3:
            string1 = string1.lower()
            string1 = ''.join(sorted(string1))
            for string2 in strings_list:
                if len(string2) >= 3:
                    string2 = string2.lower()
                    string2 = ''.join(sorted(string2))
                    if string1 == string2 and string1 != string2 and (strings_list.count(string1) >= 2):
                        anagrams_count += 1
    return anagrams_count >= 178