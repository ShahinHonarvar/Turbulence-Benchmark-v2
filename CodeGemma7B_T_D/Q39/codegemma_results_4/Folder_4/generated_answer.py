from functools import cmp_to_key

def return_n_greatest_chars(char_string):
    return sorted(char_string, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)[:90]