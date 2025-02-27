def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_found = set()
    for string1 in strings_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(string1.lower()))
        for string2 in strings_list:
            if string1 == string2:
                continue
            if len(string2) < 3:
                continue
            sorted_string2 = ''.join(sorted(string2.lower()))
            if sorted_string1 == sorted_string2 and (sorted_string1, sorted_string2) not in anagrams_found:
                anagrams_count += 1
                anagrams_found.add((sorted_string1, sorted_string2))
    return anagrams_count >= 34