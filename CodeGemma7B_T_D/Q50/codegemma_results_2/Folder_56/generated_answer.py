from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted(string.lower()))].append(string)
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) >= 3:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 77