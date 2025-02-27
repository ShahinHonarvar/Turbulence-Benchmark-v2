def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: ord(x))[:26]
    return sorted(smallest_chars, reverse=True)