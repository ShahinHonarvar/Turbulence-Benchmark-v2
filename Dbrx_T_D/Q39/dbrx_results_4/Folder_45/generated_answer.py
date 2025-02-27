def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    sorted_chars = sorted(chars_list, key=ord)[:52]
    sorted_chars.reverse()
    return sorted_chars