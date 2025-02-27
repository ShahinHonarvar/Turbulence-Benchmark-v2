import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            for other_string in string_list:
                if string != other_string and len(other_string) >= 3:
                    sorted_other_string = ''.join(sorted(other_string.lower()))
                    if sorted_string == sorted_other_string:
                        anagrams_count += 1
                        break
    return anagrams_count >= 57