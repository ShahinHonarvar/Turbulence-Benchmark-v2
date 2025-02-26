def return_n_greatest_chars(string):
    sorted_chars = sorted(list(set(string)), reverse=True)
    return sorted_chars[:28] if len(sorted_chars) >= 28 else sorted_chars