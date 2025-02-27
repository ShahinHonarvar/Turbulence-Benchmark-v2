def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_47_chars = sorted_chars[:47]
    return sorted(smallest_47_chars, reverse=True)