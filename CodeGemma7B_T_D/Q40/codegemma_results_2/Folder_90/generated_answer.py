def return_n_smallest_chars(text):
    chars = sorted([c for c in text])
    return sorted(chars, reverse=True)[:24]