def return_n_smallest_chars(s):
    return sorted(s[:52], key=ord, reverse=True)