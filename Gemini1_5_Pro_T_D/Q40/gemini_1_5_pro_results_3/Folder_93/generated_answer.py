def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s), key=ord)
    return sorted(sorted_chars[:77], reverse=True)