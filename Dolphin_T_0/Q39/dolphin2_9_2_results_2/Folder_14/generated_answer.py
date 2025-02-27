def return_n_greatest_chars(input_str):
    sorted_str = sorted(input_str, reverse=True)
    greatest_chars = sorted_str[:69]
    sorted_chars = sorted(greatest_chars)
    return sorted_chars