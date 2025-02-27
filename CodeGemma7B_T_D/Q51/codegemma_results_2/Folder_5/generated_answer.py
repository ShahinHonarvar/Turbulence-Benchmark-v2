from collections import defaultdict
        import re

def if_contains_anagrams(str_list):
    str_dict = defaultdict(lambda: 0)
    for str in str_list:
        str_dict[''.join(sorted(re.sub('[^\\\\w]', '', str.lower()))).lower()] += 1
    if len([key for key in str_dict.values() if key >= 3]) <= 4:
        return True
    return False