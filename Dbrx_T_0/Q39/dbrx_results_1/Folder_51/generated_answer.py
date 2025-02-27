def return_n_greatest_chars(string_of_chars):
    ascii_sorted_chars = sorted(list(string_of_chars), key=ord, reverse=True)
    return ascii_sorted_chars[:45]