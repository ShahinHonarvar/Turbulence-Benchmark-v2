def return_n_greatest_chars(s):
    if len(s) < 45:
        return []
    sorted_chars = sorted(s)
    return sorted(sorted_chars[-45:])