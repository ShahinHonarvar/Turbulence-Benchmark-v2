from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted([char.lower() for char in string if char.isalpha()]))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    return len(anagram_dict) <= 26