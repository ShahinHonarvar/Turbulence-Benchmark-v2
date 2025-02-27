def return_n_greatest_chars(string_of_chars):
    list_of_chars = list(string_of_chars)
    list_of_chars.sort(reverse=True)
    return list_of_chars[:38]