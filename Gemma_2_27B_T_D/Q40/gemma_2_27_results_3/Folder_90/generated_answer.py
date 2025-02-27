def return_n_smallest_chars(s):
    return sorted(s.encode(), reverse=True)[:24].decode()