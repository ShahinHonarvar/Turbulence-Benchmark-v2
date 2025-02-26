def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    smallest_chars = sorted_chars[:77] if len(sorted_chars) >= 77 else sorted_chars + [chr(0)] * (77 - len(sorted_chars))
    return sorted(smallest_chars, reverse=True)