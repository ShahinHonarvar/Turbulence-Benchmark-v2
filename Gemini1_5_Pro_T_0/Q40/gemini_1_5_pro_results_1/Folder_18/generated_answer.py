def return_n_smallest_chars(text):
    return sorted([c for c in text if ord(c) > 0 and ord(c) < 128][:52], reverse=True)