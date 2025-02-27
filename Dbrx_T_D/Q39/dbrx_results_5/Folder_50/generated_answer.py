def return_n_greatest_chars(string):
    chars_list = list(string)
    sorted_chars = sorted(chars_list, key=ord, reverse=True)[:16]
    return sorted_chars