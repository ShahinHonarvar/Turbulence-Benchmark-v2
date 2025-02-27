def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_dict:
                count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return count >= 77