def return_n_smallest_chars(str):
    return sorted([x for x in str], key=ord)[:36]