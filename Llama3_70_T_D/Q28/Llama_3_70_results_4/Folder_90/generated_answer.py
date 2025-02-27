def return_nth_smallest_ascii(s):
    s = s[:84]
    s = s[17:]
    s = sorted(s)
    return s[4]