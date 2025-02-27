import string

def if_contains_anagrams(list_of_strings):
    anagrams_counter = 0
    anagrams_set = set()
    for string_to_check in list_of_strings:
        if len(string_to_check) >= 3 and string_to_check not in anagrams_set:
            string_lower = string_to_check.lower()
            string_sorted = sorted(string_lower)
            sorted_string = ''.join(string_sorted)
            if sorted_string not in anagrams_set:
                anagrams_set.add(sorted_string)
            else:
                anagrams_counter += 1
    return anagrams_counter >= 115