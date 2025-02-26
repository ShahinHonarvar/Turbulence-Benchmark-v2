def return_n_smallest_chars(s):
    sorted_chars = sorted(list(set(s)))
    return sorted_chars[:37] if len(sorted_chars) >= 37 else sorted_chars