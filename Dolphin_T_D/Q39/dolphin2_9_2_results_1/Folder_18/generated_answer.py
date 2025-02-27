def return_n_greatest_chars(input_string):
    ascii_list = sorted([char for char in input_string], key=lambda x: ord(x), reverse=True)
    return ascii_list[:52]