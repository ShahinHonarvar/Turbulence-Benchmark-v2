from functools import cmp_to_key

def return_n_smallest_chars(char_str):
    list_of_c = sorted(char_str, key=cmp_to_key(lambda a, b: ord(a) - ord(b)), reverse=True)
    return list_of_c[:59]