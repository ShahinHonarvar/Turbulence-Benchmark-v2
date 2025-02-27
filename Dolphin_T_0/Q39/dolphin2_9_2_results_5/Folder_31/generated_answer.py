def return_n_greatest_chars(input_str):
    chars_list = list(input_str)
    chars_list.sort(reverse=True)
    return chars_list[:70]