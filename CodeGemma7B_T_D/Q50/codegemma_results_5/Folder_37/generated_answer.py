def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    for count in anagram_dict.values():
        if count >= 29:
            return True
    return False