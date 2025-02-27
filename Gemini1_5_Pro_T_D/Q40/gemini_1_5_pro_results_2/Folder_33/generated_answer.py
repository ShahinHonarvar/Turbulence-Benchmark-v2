def return_n_smallest_chars(text):
    return sorted([c for c in text if ord(c) >= ord(' ') and ord(c) <= ord('~')], reverse=True)[:36]