def return_n_smallest_chars(unique_chars):
    unique_chars = list(unique_chars)
    unique_chars.sort()
    unique_chars = unique_chars[:65]
    unique_chars.sort(reverse=True)
    return unique_chars