def return_n_smallest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[:64] if len(sorted_chars) >= 64 else sorted_chars + [chr(0)] * (64 - len(sorted_chars))