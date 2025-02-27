def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1.lower() == string2.lower() and string1 != string2 and (len(string1) >= 3) and (len(set(string1.lower())) != len(string1.lower())):
                anagrams_count += 1
                if anagrams_count > 39:
                    return False
    return anagrams_count <= 39