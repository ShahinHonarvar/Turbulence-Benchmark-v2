from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams[string].append(string)
    return len(anagrams) <= 40