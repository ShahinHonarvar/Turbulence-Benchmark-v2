def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string1 in list_of_strings:
        if len(string1) >= 3:
            sorted_string1 = ''.join(sorted(string1.lower()))
            for string2 in list_of_strings:
                if string1 != string2 and len(string2) >= 3:
                    sorted_string2 = ''.join(sorted(string2.lower()))
                    if sorted_string1 == sorted_string2:
                        anagrams_count += 1
                        break
    return anagrams_count >= 64