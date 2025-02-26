def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return sorted_chars[:40] if len(sorted_chars) >= 40 else sorted_chars