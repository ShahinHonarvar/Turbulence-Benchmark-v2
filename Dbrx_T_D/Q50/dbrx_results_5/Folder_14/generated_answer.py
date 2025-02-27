def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            for other_string in list_of_strings:
                if string != other_string and len(other_string) >= 3:
                    sorted_other_string = ''.join(sorted(other_string.lower()))
                    if sorted_string == sorted_other_string:
                        anagrams_count += 1
                        break
    return anagrams_count >= 22