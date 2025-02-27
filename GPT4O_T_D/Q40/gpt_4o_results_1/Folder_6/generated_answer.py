def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters)[:47]
    return sorted(sorted_chars, reverse=True)