def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    selected_chars = sorted_chars[:56]
    return sorted(selected_chars, reverse=True)