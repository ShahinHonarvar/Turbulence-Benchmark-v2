def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string1 in list_of_strings:
        if len(string1) < 3:
            continue
        sorted_string1 = sorted(string1.lower())
        for string2 in list_of_strings:
            if string1 == string2:
                continue
            if sorted(string2.lower()) == sorted_string1:
                anagrams_count += 1
                break
    return anagrams_count >= 8