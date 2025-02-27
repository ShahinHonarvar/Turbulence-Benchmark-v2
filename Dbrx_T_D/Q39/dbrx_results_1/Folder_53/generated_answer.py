def return_n_greatest_chars(input_str):
    chars_list = sorted(set(input_str), reverse=True)[:19]
    return sorted(chars_list)