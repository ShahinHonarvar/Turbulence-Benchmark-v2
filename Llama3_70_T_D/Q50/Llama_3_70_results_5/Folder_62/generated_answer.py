def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count >= 43