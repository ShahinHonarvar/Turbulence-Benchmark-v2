import itertools

def return_n_smallest_chars(char_str):
    return sorted(char_str, key=ord, reverse=True)[:89]