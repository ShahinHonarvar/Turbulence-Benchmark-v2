def return_n_smallest_chars(s):
    return sorted([c for c in sorted(s)][:76], reverse=True)