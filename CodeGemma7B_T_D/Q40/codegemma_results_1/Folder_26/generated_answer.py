def return_n_smallest_chars(text):
    return sorted([c for c in text], key=ord)[:43]