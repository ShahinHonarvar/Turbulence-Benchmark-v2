def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars), key=ord, reverse=True)
    return sorted_chars[:29]