def return_nth_smallest_ascii(s):
    s = s[25:65]
    ascii_values = sorted([ord(c) for c in s])
    nth_smallest_ascii_value = ascii_values[5]
    for char in s:
        if ord(char) == nth_smallest_ascii_value:
            return char