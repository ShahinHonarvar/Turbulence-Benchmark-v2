def return_n_smallest_chars(s):
    ascii_sorted = sorted(list(set(s)), key=ord)[:35]
    return sorted(ascii_sorted)