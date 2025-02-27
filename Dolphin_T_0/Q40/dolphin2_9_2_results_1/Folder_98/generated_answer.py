def return_n_smallest_chars(s):
    return sorted(s, key=lambda v: ord(v), reverse=True)[:68]