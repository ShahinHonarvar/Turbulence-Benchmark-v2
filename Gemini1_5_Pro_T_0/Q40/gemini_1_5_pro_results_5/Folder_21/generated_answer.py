def return_n_smallest_chars(text):
    sorted_chars = sorted(text)
    smallest_chars = sorted_chars[:44]
    smallest_chars.sort(reverse=True)
    return smallest_chars