from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        anagram_key = ''.join(sorted(string.lower()))
        if len(anagram_key) >= 3:
            anagram_dict[anagram_key].append(string)
    num_anagrams = 0
    for anagrams in anagram_dict.values():
        num_anagrams += len(anagrams) * (len(anagrams) - 1) // 2
    return num_anagrams >= 74