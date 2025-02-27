def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_56_chars = sorted_chars[:56]
    return sorted(smallest_56_chars, reverse=True)