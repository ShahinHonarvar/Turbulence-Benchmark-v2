from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(int)
    for string in str_list:
        if len(string) >= 3:
            str_dict[''.join(sorted(string.lower()))] += 1
    if any((count >= 194 for count in str_dict.values())):
        return True
    return False