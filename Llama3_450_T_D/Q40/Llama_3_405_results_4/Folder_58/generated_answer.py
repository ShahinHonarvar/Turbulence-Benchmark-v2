def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    n_smallest_chars = sorted_chars[:49]
    result = sorted(n_smallest_chars, reverse=True)
    return result