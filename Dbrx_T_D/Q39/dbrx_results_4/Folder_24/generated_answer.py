def return_n_greatest_chars(input_string):
    ascii_sorted_chars = sorted(input_string, key=ord, reverse=True)
    return ascii_sorted_chars[:32]