from collections import defaultdict

def if_contains_anagrams(str_list):
    dict_anagrams = defaultdict(list)
    for str in str_list:
        str = ''.join(sorted(str.lower()))
        if len(str) >= 3:
            dict_anagrams[str].append(str)
    count = 0
    for group in dict_anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 97