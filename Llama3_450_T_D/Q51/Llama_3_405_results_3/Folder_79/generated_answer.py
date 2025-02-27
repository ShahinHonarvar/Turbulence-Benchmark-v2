def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        lower_string = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count <= 173