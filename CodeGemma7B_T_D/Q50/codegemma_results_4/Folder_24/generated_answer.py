from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(list)
    for string in str_list:
        char_list = list(string.lower())
        char_list.sort()
        key = ''.join(char_list)
        str_map[key].append(string)
    pairs = 0
    for anagrams in str_map.values():
        if len(anagrams) >= 3:
            pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs >= 65