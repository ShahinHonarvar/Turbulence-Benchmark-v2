def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters)
    smallest_chars = sorted_chars[:20]
    return smallest_chars[::-1]