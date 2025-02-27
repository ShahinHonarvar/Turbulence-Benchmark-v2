def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda c: ord(c))
    return sorted(sorted_chars, key=lambda c: -ord(c))[:64]