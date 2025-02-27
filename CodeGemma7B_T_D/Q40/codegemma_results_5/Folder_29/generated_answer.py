def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters, key=ord)
    return sorted_chars[:23][::-1]