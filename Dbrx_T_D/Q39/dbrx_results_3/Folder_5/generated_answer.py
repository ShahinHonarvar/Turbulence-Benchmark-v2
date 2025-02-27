def return_n_greatest_chars(string_of_chars):
    ascii_sorted_chars = sorted(string_of_chars, key=ord)
    return ascii_sorted_chars[-46:]