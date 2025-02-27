from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for str_to_check in list_of_strings:
        if len(str_to_check) < 3:
            continue
        sorted_string = ''.join(sorted(str_to_check.lower()))
        anagram_dict[sorted_string].append(str_to_check)
    num_anagrams = 0
    for key in anagram_dict:
        num_anagrams += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if num_anagrams > 147:
            return False
    return True