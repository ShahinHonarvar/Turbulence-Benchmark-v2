def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagram_dict and len(string) >= 3 and string.isalpha():
            anagram_dict[sorted_str] += 1
        elif len(string) >= 3 and string.isalpha():
            anagram_dict[sorted_str] = 1
    for key in anagram_dict:
        if anagram_dict[key] > 1:
            count += 1
    return count <= 4