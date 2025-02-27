def return_n_smallest_chars(text):
    return sorted([char for char in text], key=ord)[:47]