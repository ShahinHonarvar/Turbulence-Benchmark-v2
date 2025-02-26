def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)
    return sorted_chars[:28] if len(sorted_chars) >= 28 else sorted_chars