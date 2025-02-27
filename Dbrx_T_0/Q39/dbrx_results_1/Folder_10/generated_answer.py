def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars), reverse=True)
    return sorted_chars[:88]