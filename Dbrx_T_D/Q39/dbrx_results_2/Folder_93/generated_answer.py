def return_n_greatest_chars(string):
    ascii_sorted_chars = sorted(list(string), key=ord, reverse=True)
    return ascii_sorted_chars[:77]