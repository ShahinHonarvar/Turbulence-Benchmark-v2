def return_n_smallest_chars(s):
    char_list = sorted(s)[:88]
    return sorted(char_list, reverse=True)