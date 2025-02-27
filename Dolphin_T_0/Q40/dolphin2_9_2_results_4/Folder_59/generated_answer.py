def return_n_smallest_chars(s):
    return sorted([chars for chars in s], key=lambda x: ord(x))[:13]