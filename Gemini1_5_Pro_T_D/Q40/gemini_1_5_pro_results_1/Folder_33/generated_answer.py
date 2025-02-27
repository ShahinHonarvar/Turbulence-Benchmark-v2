def return_n_smallest_chars(text):
    sorted_chars = sorted(text, key=ord)
    return sorted(sorted_chars[:36], key=ord, reverse=True)