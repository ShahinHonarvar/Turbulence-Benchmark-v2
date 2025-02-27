def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    sorted_chars = sorted(chars_list, reverse=True)[:33]
    return sorted_chars