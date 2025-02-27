def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:38]
    sorted_chars.reverse()
    return sorted_chars