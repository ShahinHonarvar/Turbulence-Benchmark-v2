def return_n_smallest_chars(s):
    return sorted([c for c in s], key=lambda c: ord(c), reverse=True)[:35]