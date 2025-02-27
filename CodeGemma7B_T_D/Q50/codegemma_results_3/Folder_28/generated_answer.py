from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        str_dict[sorted_string].append(string)
    anagram_count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 2:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    if anagram_count >= 81:
        return True
    else:
        return False