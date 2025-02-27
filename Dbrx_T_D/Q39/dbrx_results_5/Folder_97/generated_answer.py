def return_n_greatest_chars(string_of_chars):
    ascii_sorted_list = sorted([char for char in set(string_of_chars)], reverse=True)
    return ascii_sorted_list[:38]