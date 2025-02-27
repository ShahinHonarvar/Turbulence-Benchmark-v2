def return_n_greatest_chars(string):
    ascii_sorted_list = sorted(list(set(string)), key=ord, reverse=True)
    return ascii_sorted_list[:23]