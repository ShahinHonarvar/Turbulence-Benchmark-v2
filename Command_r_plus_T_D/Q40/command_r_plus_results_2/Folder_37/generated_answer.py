def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: ord(x))[:26]
    smallest_chars.reverse()
    return smallest_chars