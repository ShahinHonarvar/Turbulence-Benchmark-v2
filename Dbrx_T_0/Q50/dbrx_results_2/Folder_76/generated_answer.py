import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string_length in range(3, len(strings_list[0]) + 1):
        for string_tuple in itertools.combinations(strings_list, string_length):
            sorted_strings = [''.join(sorted(string.lower())) for string in string_tuple]
            if len(sorted_strings) > len(set(sorted_strings)):
                anagrams_count += 1
                if anagrams_count >= 143:
                    return True
    return False