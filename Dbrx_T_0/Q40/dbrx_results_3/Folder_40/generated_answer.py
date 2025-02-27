def return_n_smallest_chars(string):
    chars = sorted(set(string))
    return chars[:7][::-1]