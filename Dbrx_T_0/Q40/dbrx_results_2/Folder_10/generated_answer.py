def return_n_smallest_chars(string):
    chars_list = sorted(list(string), key=ord)[:88]
    return sorted(chars_list, reverse=True)