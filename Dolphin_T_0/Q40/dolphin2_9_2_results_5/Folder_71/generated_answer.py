def return_n_smallest_chars(text):
    return sorted(text, key=lambda c: ord(c))[:14]