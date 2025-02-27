from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(int)
    for str in str_list:
        str_dict[''.join(sorted([ch.lower() for ch in str if ch.isalpha() and len(ch) >= 3]))] += 1
    return sum((count for count in str_dict.values() if count > 1)) <= 21