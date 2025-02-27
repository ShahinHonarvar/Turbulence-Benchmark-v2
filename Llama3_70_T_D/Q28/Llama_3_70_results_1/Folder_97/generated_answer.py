def return_nth_smallest_ascii(s):
    substring = s[15:22]
    ascii_values = sorted([ord(c) for c in substring])
    sixth_smallest_ascii = ascii_values[5]
    for c in substring:
        if ord(c) == sixth_smallest_ascii:
            return c