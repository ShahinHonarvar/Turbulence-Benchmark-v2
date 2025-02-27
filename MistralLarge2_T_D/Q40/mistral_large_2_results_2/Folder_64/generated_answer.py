def return_n_smallest_chars(s):
    return sorted([char for char in s], key=lambda c: ord(c))[:39][::-1]