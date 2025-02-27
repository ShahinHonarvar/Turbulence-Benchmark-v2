from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    anagram_count = 0
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        if sorted_str in str_dict:
            str_dict[sorted_str].append(string)
            anagram_count += 1
        else:
            str_dict[sorted_str] = [string]
    return anagram_count <= 206