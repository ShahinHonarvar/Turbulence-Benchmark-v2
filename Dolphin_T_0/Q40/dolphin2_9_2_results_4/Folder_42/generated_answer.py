def return_n_smallest_chars(s):
    return sorted([ch for ch in s], key=lambda ch: ord(ch), reverse=True)[:59]