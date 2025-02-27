def return_n_smallest_chars(s):
    return sorted([c for c in s], key=lambda v: ord(v), reverse=True)[:38]