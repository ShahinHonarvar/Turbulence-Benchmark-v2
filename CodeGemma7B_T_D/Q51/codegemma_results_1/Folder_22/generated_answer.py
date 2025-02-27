from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    seen_anagrams = set()
    for string in str_list:
        if len(string) < 3 or not all((c.isalpha() for c in string)):
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in str_dict and len(str_dict[sorted_str]) > 0:
            seen_anagrams.add(tuple(sorted_str))
        str_dict[sorted_str].append(string)
    return len(seen_anagrams) <= 14