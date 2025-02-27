from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    count = 0
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in str_dict:
            str_dict[sorted_string].append(string)
        else:
            count += len(str_dict[sorted_string])
            str_dict[sorted_string].append(string)
    return count <= 57