def return_n_smallest_chars(s):
    sorted_chars_set = sorted(s, key=lambda x: ord(x))[:29]
    sorted_chars_list = sorted(sorted_chars_set)
    return sorted_chars_list