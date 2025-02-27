def return_n_smallest_chars(str):
    return sorted([c for c in str[:7]], key=ord)