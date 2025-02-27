from collections import defaultdict

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    char_to_strings = defaultdict(list)
    for s in str_list:
        sorted_str = ''.join(sorted(s))
        char_to_strings[sorted_str].append(s)
    pairs_count = 0
    for string_list in char_to_strings.values():
        pairs_count += len(string_list) * (len(string_list) - 1) // 2
    return pairs_count >= 123