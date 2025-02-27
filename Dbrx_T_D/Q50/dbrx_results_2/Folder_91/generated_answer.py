def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1 in string_list:
        if len(string1) < 3:
            continue
        sorted_string1 = sorted(string1.lower())
        for string2 in string_list:
            if string1 == string2 or len(string2) < 3:
                continue
            sorted_string2 = sorted(string2.lower())
            if sorted_string1 == sorted_string2:
                anagrams_count += 1
                break
    return anagrams_count >= 6