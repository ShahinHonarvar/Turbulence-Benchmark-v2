def return_n_greatest_chars(input_string):
    sorted_chars = sorted([char for char in input_string], reverse=True)
    return sorted_chars[:76]