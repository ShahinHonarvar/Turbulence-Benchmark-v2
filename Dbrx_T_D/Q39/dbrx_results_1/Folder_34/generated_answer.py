def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars))[-9:]
    return sorted_chars[::-1]