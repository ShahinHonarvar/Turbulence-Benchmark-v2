def return_n_greatest_chars(input_str):
    return sorted([char for char in input_str], reverse=True)[:24]