def return_n_greatest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars)
    return sorted_chars[-37:]