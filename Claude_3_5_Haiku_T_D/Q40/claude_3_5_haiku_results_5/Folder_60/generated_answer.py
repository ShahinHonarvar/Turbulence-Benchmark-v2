def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    return sorted_chars[:28] if len(sorted_chars) >= 28 else sorted_chars