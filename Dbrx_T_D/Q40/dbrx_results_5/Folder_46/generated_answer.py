def return_n_smallest_chars(string):
    chars_list = sorted(list(set(string)), key=ord)
    return chars_list[-54:][::-1]