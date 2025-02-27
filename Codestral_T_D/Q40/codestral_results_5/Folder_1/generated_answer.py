def return_n_smallest_chars(s):
    return sorted(list(s)[:11], key=ord, reverse=True)