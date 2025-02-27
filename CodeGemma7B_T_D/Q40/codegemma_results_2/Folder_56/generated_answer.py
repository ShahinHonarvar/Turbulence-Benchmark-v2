from functools import cmp_to_key

def return_n_smallest_chars(string_values):
    char_list = list(string_values)
    char_list.sort(key=cmp_to_key(lambda a, b: ord(a) - ord(b)))
    return char_list[:21]