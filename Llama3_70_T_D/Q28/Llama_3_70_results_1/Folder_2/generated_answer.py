def return_nth_smallest_ascii(s):
    s = s[48:77]
    s = ''.join(sorted(s))
    return s[4]