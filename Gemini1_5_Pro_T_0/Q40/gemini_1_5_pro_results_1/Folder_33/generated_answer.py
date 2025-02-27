def return_n_smallest_chars(text):
    return sorted([c for c in text], reverse=True)[:36]