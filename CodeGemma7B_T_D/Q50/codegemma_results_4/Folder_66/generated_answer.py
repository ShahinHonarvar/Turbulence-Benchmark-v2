from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            str_dict[sorted_str].append(string)
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) >= 2:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 92