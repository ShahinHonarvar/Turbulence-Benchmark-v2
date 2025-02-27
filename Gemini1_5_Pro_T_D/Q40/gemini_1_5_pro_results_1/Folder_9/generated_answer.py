def return_n_smallest_chars(text):
    sorted_chars = sorted(text, key=ord)
    return sorted_chars[:20]