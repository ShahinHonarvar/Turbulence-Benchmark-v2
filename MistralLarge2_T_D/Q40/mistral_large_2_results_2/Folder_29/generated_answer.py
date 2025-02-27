def return_n_smallest_chars(s):
    return sorted(s[:23], key=ord, reverse=True)