def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1 == string2:
                continue
            if len(string1) < 3 or len(string2) < 3:
                continue
            if sorted(string1.lower()) == sorted(string2.lower()):
                anagrams_count += 1
                if anagrams_count > 61:
                    return False
    return True