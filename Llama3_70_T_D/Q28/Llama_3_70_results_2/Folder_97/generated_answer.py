def return_nth_smallest_ascii(s):
    substring = s[15:22]
    ascii_values = sorted([ord(c) for c in substring])
    nth_smallest_ascii = ascii_values[5]
    for char in substring:
        if ord(char) == nth_smallest_ascii:
            return char