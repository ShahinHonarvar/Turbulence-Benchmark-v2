from functools import cmp_to_key

def return_n_smallest_chars(char_str):
    return sorted(char_str, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)[:37]