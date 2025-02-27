import itertools

def if_contains_anagrams(strings_list):
    anagrams_counter = 0
    for string_length in range(3, len(strings_list[0])):
        for string in strings_list:
            if len(string) >= string_length:
                sorted_characters = [''.join(sorted((char.lower() for char in part))) for part in itertools.permutations(string, string_length)]
                anagrams_counter += len(sorted_characters) - len(set(sorted_characters))
                if anagrams_counter >= 46:
                    return True
    return False