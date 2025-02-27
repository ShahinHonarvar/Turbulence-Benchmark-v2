def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    return sorted(s[:26], reverse=True)