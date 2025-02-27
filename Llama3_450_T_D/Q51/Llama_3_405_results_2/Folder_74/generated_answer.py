def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        if len(string) >= 3 and string.isalpha():
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return anagram_count <= 57