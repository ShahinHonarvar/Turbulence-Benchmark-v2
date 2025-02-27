def return_nth_smallest_ascii(s):
    s_substring = s[10:83]
    ascii_values = sorted([ord(c) for c in s_substring])
    nth_smallest_ascii = ascii_values[17]
    for c in s_substring:
        if ord(c) == nth_smallest_ascii:
            return c