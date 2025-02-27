from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        ana = ''.join(sorted(string.lower()))
        if len(ana) >= 3:
            str_dict[ana].append(string)
    count = 0
    for group in str_dict.values():
        count += len(group) - 1
    return count <= 48