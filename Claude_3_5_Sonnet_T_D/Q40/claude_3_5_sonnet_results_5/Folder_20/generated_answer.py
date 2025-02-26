def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:40] if len(sorted_chars) >= 40 else sorted_chars + [''] * (40 - len(sorted_chars))