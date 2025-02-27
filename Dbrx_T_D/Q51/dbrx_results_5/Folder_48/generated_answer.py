import collections

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string in strings_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string] += 1
            if anagrams_dict[sorted_string] == 2:
                anagrams_count += 1
        else:
            anagrams_dict[sorted_string] = 1
    return anagrams_count <= 277