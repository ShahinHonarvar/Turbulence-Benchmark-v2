from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        string = ''.join((char for char in string if char.isalpha())).lower()
        sorted_string = ''.join(sorted(string))
        anagrams[sorted_string].append(string)
    num_anagrams = 0
    for anagram_list in anagrams.values():
        num_anagrams += len(anagram_list)
    return num_anagrams <= 475