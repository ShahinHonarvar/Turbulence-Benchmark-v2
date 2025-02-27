def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars), key=ord)
    return sorted_chars[-46:]