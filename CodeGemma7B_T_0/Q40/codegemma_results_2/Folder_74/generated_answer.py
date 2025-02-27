def return_n_smallest_chars(str):
    return sorted([ch for ch in str], key=ord)[:5]