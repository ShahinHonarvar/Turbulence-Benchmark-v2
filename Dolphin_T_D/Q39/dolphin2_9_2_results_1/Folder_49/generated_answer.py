def return_n_greatest_chars(input_string):
    return sorted([c for c in input_string], reverse=True)[:76]