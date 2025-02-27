def return_n_greatest_chars(input_str):
    return sorted(input_str, key=ord, reverse=True)[:64]