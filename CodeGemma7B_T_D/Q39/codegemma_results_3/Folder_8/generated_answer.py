from functools import cmp_to_key

def return_n_greatest_chars(str_input):
    return sorted(str_input, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)[:83]