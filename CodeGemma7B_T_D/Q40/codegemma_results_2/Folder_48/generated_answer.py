def return_n_smallest_chars(text):
    return sorted([char for char in text if len(text) >= 12], key=ord)[:12]