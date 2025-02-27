def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_72_chars = sorted_chars[:72]
    return sorted(smallest_72_chars, reverse=True)