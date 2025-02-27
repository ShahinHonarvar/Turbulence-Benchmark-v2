def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))
    smallest_77_chars = sorted_chars[:77]
    result = sorted(smallest_77_chars, reverse=True)
    return result