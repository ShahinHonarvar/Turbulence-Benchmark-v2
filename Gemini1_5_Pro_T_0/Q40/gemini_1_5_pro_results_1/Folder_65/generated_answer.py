def return_n_smallest_chars(text):
    sorted_chars = sorted(text, reverse=True)
    return sorted_chars[:27]