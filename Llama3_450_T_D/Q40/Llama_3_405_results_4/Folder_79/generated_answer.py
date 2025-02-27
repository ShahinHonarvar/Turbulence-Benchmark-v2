def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_s[:82]
    return sorted(smallest_chars, reverse=True)