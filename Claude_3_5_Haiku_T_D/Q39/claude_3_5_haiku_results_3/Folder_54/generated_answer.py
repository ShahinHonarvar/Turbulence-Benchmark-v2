def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)
    return sorted_chars[:79] if len(sorted_chars) >= 79 else sorted_chars