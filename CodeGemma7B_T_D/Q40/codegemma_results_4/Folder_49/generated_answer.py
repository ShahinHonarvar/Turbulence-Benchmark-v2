from functools import cmp_to_key

def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=cmp_to_key(lambda char1, char2: char2.lower().__lt__(char1.lower())))
    return sorted_chars[:76]