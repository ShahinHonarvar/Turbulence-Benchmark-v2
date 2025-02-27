def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = 0
            anagram_dict[sorted_string] += 1
            anagram_count += anagram_dict[sorted_string] - 1
    return anagram_count >= 16