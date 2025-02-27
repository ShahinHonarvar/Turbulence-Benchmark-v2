def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_dict:
                anagram_count += anagram_dict[sorted_string]
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    return anagram_count <= 43