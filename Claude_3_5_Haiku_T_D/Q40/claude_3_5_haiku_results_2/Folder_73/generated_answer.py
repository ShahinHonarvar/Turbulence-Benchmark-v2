def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    return sorted_chars[:80] if len(sorted_chars) >= 80 else sorted_chars