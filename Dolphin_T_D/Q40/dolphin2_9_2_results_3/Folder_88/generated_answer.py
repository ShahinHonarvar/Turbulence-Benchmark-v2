def return_n_smallest_chars(s):
    return sorted([ch for ch in s if ch.isascii()][:84])