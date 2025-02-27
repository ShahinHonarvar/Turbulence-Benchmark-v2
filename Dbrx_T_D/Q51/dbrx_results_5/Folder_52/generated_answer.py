import itertools

def if_contains_anagrams(strings_list):
    anagrams_counter = 0
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for string in strings_list:
        string = string.lower()
        if len(string) < 3 or not set(string).issubset(english_letters):
            continue
        sorted_string = ''.join(sorted(string))
        for string_permutation in itertools.permutations(sorted_string):
            string_permutation = ''.join(string_permutation)
            if string_permutation != string and string_permutation in strings_list:
                anagrams_counter += 1
                break
        if anagrams_counter > 43:
            return False
    return True if anagrams_counter <= 43 else False