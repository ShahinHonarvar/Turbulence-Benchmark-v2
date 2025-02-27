def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    sorted_chars = sorted(chars_list, key=ord)
    n_greatest_chars = sorted_chars[-5:]
    return n_greatest_chars