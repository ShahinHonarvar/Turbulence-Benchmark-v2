def return_n_greatest_chars(input_string):
    return sorted([char for char in input_string], reverse=True)[:52]