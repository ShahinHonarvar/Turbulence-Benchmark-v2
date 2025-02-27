def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for string in string_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_str.isalpha():
            if sorted_str in anagram_dict:
                anagram_count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return anagram_count <= 44