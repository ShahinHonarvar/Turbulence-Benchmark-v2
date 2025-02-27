def if_contains_anagrams(strings_list):
    anagrams_dict = {}
    for string in strings_list:
        sorted_string = ''.join(sorted((c.lower() for c in string if c.isalpha())))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string] += 1
            if anagrams_dict[sorted_string] > 289:
                return True
        else:
            anagrams_dict[sorted_string] = 1
    return False