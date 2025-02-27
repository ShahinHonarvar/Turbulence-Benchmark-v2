def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
    return count <= 35