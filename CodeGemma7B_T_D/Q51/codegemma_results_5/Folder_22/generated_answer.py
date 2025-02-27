from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(set)
    for string in str_list:
        key = ''.join(sorted([char for char in string.lower() if char.isalpha() and len(char) >= 3]))
        anagrams[key].add(string)
    return len(anagrams) <= 14