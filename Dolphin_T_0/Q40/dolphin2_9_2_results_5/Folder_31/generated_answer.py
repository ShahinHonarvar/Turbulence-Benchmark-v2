def return_n_smallest_chars(chars):
    return sorted(chars, key=lambda x: ord(x), reverse=True)[:70]