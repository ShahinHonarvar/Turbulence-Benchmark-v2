def return_n_greatest_chars(string_of_chars):
    return sorted(list(string_of_chars), key=ord, reverse=True)[:90]