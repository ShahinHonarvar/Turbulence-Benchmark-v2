def return_n_greatest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, reverse=True)
    return sorted_chars[:52]