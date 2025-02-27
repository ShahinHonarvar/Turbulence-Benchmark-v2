from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_string = sorted(string.lower())
        anagrams[''.join(sorted_string)].append(string)
    num_anagrams = 0
    for group in anagrams.values():
        num_anagrams += len(group) * (len(group) - 1) // 2
    return num_anagrams >= 85