from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(int)
    for string in str_list:
        str_set = set(string.lower()).difference('abcdefghijklmnopqrstuvwxyz')
        for char in str_set:
            string = string.replace(char, '')
        anagrams[tuple(sorted(string))] += 1
    return sum((count - 1 for count in anagrams.values() if count > 1)) <= 21