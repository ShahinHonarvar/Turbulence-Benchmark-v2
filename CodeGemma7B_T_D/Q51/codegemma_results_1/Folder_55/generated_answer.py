from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted((c for c in string.lower() if c.isalpha())))
        anagram_dict[sorted_string].append(string)
    return len(anagram_dict) <= 44