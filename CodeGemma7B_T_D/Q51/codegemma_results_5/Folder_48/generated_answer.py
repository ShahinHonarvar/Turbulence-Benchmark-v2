from collections import defaultdict

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted([char for char in s1 if char.isalpha()])
    s2_sorted = sorted([char for char in s2 if char.isalpha()])
    return s1_sorted == s2_sorted

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        str_dict[tuple(sorted([char for char in s.lower() if char.isalpha()]))].append(s)
    return len(str_dict) <= 277