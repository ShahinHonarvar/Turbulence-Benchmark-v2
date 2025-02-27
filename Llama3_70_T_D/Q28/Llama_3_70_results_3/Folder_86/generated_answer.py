def return_nth_smallest_ascii(s):
    substring = s[44:70]
    ascii_values = sorted([ord(char) for char in substring])
    nth_smallest_ascii = ascii_values[14]
    for char in substring:
        if ord(char) == nth_smallest_ascii:
            return char