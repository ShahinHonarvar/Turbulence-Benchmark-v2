def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return sorted_chars[:66] if len(sorted_chars) >= 66 else sorted_chars