from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            str_dict[key].append(word)
    for sublist in str_dict.values():
        if len(sublist) > 475:
            return False
    return True