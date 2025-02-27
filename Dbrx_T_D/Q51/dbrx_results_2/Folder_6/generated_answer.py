import collections

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
            if anagram_dict[sorted_string] == 2:
                anagram_count += 1
        else:
            anagram_dict[sorted_string] = 1
    return anagram_count <= 86