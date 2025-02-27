def return_n_smallest_chars(characters):
    sorted_chars = sorted(characters)
    smallest_chars = sorted_chars[:37]
    smallest_chars.reverse()
    return smallest_chars