def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    result = sorted_chars[:64] if len(sorted_chars) >= 64 else sorted_chars + list(set(s) - set(sorted_chars))
    return sorted(result, reverse=True)