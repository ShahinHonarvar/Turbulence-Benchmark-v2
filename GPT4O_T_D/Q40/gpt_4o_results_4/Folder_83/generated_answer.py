def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters)
    smallest_chars = sorted_chars[:38]
    return sorted(smallest_chars, reverse=True)