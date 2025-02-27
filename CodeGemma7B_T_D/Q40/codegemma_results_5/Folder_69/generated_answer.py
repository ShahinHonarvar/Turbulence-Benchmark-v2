def return_n_smallest_chars(a):
    return sorted(a, key=ord, reverse=True)[:65]