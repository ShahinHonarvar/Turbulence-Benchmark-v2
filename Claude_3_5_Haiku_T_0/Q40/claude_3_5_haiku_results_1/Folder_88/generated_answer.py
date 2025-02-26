def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars + [sorted_chars[-1]] * (84 - len(sorted_chars))