from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(int)
    for str in str_list:
        str_lower = ''.join(sorted(str.lower()))
        if len(str) >= 3 and str_lower not in anagram_dict:
            anagram_dict[str_lower] = 1
    return len(anagram_dict) <= 116