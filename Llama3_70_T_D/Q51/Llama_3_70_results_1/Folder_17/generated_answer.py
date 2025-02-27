def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    anagram_count = 0
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and (sorted_string in anagram_dict and anagram_dict[sorted_string] != string.lower()):
            anagram_count += 1
        anagram_dict[sorted_string] = string.lower()
    return anagram_count <= 22