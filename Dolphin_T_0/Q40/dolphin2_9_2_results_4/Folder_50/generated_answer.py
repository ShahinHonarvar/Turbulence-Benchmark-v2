def return_n_smallest_chars(s):
    sorted_chars = sorted([c for c in s], key=lambda c: ord(c), reverse=True)
    return sorted_chars[:16]