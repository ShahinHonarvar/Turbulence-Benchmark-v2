def return_n_smallest_chars(str):
    return sorted([char for char in str], key=ord)[:35]