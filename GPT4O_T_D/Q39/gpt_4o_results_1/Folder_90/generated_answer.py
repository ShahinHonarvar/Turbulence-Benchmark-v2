def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    return sorted_chars[:24] if len(sorted_chars) >= 24 else sorted_chars