def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted_chars[:80] if len(sorted_chars) >= 80 else sorted_chars