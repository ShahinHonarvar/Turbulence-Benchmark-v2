def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:12]
    return char_list.ljust(12, chr(126))