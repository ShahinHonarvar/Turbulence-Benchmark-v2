def return_n_smallest_chars(str):
    return sorted([c for c in str], key=ord, reverse=True)[:64]