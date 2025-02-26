def return_n_smallest_chars(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=ord)[:65]
    return sorted(sorted_chars, reverse=True)