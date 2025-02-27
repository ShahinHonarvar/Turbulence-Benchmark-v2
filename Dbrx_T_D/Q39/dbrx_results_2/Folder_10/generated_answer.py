def return_n_greatest_chars(string):
    chars_list = sorted(list(set(string)), reverse=True)
    return chars_list[:88]