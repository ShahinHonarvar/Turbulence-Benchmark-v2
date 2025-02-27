from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    return len(anagrams) <= 34