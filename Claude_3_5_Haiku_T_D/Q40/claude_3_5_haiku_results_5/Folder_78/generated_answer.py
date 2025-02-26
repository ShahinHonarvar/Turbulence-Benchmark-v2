def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s), key=lambda x: ord(x))[:43]
    return sorted(sorted_chars, reverse=True)