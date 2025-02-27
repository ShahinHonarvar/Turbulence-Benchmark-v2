def return_nth_smallest_ascii(s):
    s = s[33:86]
    ascii_values = sorted([ord(c) for c in s])
    nth_smallest_ascii = ascii_values[12]
    for char in s:
        if ord(char) == nth_smallest_ascii:
            return char