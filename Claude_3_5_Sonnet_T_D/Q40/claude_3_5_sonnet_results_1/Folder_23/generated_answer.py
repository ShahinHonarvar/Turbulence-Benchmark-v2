def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    return sorted_chars[:46] if len(sorted_chars) >= 46 else sorted_chars + [''] * (46 - len(sorted_chars))