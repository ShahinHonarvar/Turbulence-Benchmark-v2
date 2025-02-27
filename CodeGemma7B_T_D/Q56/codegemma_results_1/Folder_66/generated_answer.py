from itertools import combinations_with_replacement

def all_substring_of_size_n(s: str) -> list:
    str_len = len(s)
    if str_len < 26:
        return []
    combinations_list = list(combinations_with_replacement(s, 26))
    all_possible_substring = [''.join(c) for c in combinations_list]
    unique_substring = list(set(all_possible_substring))
    return unique_substring