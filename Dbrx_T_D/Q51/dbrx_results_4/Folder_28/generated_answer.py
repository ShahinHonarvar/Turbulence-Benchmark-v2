def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1.lower() == string2.lower():
                continue
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                anagrams_count += 1
                if anagrams_count > 78:
                    return False
    return True