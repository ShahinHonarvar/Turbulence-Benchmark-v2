def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    return s[len(s) - 24:len(s) - 1][::-1]