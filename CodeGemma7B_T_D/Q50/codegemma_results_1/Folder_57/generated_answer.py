from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        str_dict[tuple(sorted(word.lower()))].append(word)
    num_anagrams = 0
    for anagram_list in str_dict.values():
        num_anagrams += len(anagram_list) * (len(anagram_list) - 1) // 2
    return num_anagrams >= 50