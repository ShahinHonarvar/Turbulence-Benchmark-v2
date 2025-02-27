from typing import List

def if_contains_anagrams(str_list: List[str]) -> bool:
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in str_dict:
            str_dict[sorted_string] = 1
        elif len(sorted_string) >= 3 and sorted_string in str_dict:
            str_dict[sorted_string] += 1
    pairs = sum((count // 2 for count in str_dict.values() if count >= 2))
    return pairs >= 74