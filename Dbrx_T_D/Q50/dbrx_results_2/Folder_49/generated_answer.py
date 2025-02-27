def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1 in string_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower()))
        for string2 in string_list:
            if len(string2) < 3 or string1 == string2:
                continue
            sorted_string2 = ''.join(sorted(string2.lower()))
            if sorted_string1 == sorted_string2:
                anagrams_count += 1
    return anagrams_count >= 59