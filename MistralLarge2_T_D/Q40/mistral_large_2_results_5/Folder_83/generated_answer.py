def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_38_chars = sorted_chars[:38]
    return sorted(smallest_38_chars, reverse=True)