def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return anagram_count <= 17