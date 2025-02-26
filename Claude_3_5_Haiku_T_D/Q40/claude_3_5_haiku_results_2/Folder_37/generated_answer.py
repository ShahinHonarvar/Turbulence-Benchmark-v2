def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort()
    return sorted(chars[:26], reverse=True)