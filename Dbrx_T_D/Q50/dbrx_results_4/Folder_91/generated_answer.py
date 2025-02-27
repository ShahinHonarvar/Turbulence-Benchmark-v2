def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string_1 in strings_list:
        if len(string_1) < 3:
            continue
        sorted_1 = ''.join(sorted(string_1.lower()))
        for string_2 in strings_list:
            if string_1 == string_2:
                continue
            if len(string_2) < 3:
                continue
            sorted_2 = ''.join(sorted(string_2.lower()))
            if sorted_1 == sorted_2:
                anagrams_count += 1
    return anagrams_count >= 6