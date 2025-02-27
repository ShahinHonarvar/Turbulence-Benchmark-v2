def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))[:70]
    return sorted(sorted_chars, reverse=True)