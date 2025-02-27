from collections import defaultdict

def if_contains_anagrams(str_list):

    def is_valid(str):
        return len(str) >= 3

    def anagram_key(str):
        return tuple(sorted(str.lower()))
    anagrams = defaultdict(list)
    for string in str_list:
        if is_valid(string):
            anagrams[anagram_key(string)].append(string)
    return len(anagrams) >= 67