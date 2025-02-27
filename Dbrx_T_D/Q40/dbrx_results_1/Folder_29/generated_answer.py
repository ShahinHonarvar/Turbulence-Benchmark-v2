def return_n_smallest_chars(s):
    ascii_sorted = sorted(list(set(s)), key=ord)
    return ascii_sorted[:23][::-1]