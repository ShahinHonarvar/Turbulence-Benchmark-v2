def return_n_greatest_chars(s):
    if len(s) < 17:
        return sorted(list(s))
    sorted_chars = sorted(s, reverse=True)
    return sorted(sorted_chars[:17])