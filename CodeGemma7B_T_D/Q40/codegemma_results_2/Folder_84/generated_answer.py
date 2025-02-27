def return_n_smallest_chars(ch):
    return sorted([c for c in ch], key=ord)[:10]