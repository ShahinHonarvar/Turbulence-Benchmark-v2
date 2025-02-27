def if_contains_anagrams(string_list):
    string_list = [string.lower() for string in string_list]
    anagram_dict = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    count = 0
    for value in anagram_dict.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 55