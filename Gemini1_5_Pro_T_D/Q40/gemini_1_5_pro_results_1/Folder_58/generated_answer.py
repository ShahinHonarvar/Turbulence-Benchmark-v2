def return_n_smallest_chars(text):
    return sorted([c for c in text if ord(c) <= 122][:49], reverse=True)