def return_n_smallest_chars(arg):
    return sorted(arg, key=ord, reverse=True)[:7]