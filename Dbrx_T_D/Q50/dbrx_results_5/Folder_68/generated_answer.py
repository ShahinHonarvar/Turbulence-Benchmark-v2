import collections

def if_contains_anagrams(list_of_strings):
    anagrams_counter = 0
    anagram_length = 3
    for string in list_of_strings:
        if len(string) < anagram_length:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        list_of_strings[list_of_strings.index(string)] = sorted_string
    anagrams_dict = collections.defaultdict(list)
    for string in list_of_strings:
        anagrams_dict[string].append(string)
    for anagrams_list in anagrams_dict.values():
        if len(anagrams_list) >= 2:
            anagrams_counter += 1
    if anagrams_counter >= 9:
        return True
    else:
        return False