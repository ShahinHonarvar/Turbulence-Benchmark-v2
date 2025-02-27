def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(sorted_string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_dict:
                count += anagram_dict[sorted_string]
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    return count <= 68