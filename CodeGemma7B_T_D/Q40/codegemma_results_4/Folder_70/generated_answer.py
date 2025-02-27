def return_n_smallest_chars(char_str):
    sorted_str = ''.join(sorted(char_str))
    return sorted_str[:2]