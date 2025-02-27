from functools import cmp_to_key

def return_n_smallest_chars(text):
    ascii_values = sorted(list(text), key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)
    return ascii_values[:29]