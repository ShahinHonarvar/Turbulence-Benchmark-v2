def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    return sorted(s[:75], reverse=True)