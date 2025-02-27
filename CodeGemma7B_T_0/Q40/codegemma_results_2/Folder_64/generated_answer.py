def return_n_smallest_chars(text):
    return sorted(text, key=ord, reverse=True)[:39]