def return_nth_smallest_ascii(s):
    s = s[33:61]
    s = sorted(set(s))
    return s[17]