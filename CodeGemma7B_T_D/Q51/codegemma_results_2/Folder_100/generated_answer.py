from collections import Counter

def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        filtered_string = ''.join((c for c in string.lower() if c.isalpha() and len(string) >= 3))
        str_dict[filtered_string] = str_dict.get(filtered_string, 0) + 1
    anagram_pairs = 0
    for count in str_dict.values():
        if count > 1:
            anagram_pairs += (count - 1) * count // 2
    return anagram_pairs <= 98