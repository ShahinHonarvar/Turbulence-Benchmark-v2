def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(string_of_chars, key=ord, reverse=True)
    return sorted_chars[:84]