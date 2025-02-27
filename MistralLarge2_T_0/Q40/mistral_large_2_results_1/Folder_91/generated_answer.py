def return_n_smallest_chars(s):
    return sorted(s, key=ord)[:6][::-1]