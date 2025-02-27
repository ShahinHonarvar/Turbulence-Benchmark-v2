def if_contains_anagrams(list_of_strings):
    counter = 0
    for string in list_of_strings:
        if len(string) >= 3:
            for compare_string in list_of_strings:
                if string.lower() != compare_string.lower() and sorted(string.lower()) == sorted(compare_string.lower()):
                    counter += 1
    return counter >= 40