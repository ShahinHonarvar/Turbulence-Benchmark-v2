import collections

def if_contains_anagrams(strings_list):
    anagrams_counter = 0
    anagrams_dict = {}
    for string in strings_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams_dict:
            anagrams_dict[sorted_string] = [string]
        else:
            anagrams_dict[sorted_string].append(string)
            anagrams_counter += 1
    return anagrams_counter >= 140