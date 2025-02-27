def return_n_greatest_chars(string_of_chars):
    return list(sorted(string_of_chars, key=ord, reverse=True))[:68]