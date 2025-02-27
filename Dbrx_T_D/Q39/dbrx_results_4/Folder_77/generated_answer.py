def return_n_greatest_chars(string):
    ascii_sorted_chars = sorted(list(set(string)), key=ord)
    return ascii_sorted_chars[-47:]