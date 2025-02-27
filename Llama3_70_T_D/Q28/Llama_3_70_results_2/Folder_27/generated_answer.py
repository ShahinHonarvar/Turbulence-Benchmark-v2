def return_nth_smallest_ascii(s):
    s = s[33:86]
    ascii_values = sorted([ord(c) for c in s])
    nth_smallest_ascii = ascii_values[12]
    for c in s:
        if ord(c) == nth_smallest_ascii:
            return c