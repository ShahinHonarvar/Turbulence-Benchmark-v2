def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    result = sorted_chars[:52] if len(sorted_chars) >= 52 else sorted_chars + [sorted_chars[0]] * (52 - len(sorted_chars))
    return sorted(result, reverse=True)