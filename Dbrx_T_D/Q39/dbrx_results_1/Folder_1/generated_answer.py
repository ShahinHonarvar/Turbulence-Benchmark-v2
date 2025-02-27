def return_n_greatest_chars(string_of_chars):
    unique_chars = list(set(string_of_chars))
    unique_chars.sort(reverse=True)
    return unique_chars[:11]