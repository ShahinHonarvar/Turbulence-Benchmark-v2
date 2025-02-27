import collections

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string in strings_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
            if anagram_dict[sorted_string] == 2:
                anagrams_count += 1
        else:
            anagram_dict[sorted_string] = 1
    return anagrams_count <= 416