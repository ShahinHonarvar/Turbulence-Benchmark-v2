def return_n_smallest_chars(s):
    chars = list(set(s))
    sorted_chars = sorted(chars, key=ord)[:66]
    return sorted(sorted_chars, reverse=True)