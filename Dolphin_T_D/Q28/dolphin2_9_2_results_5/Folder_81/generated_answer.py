def return_nth_smallest_ascii(s):
    chars = list(s[0:14])
    ascii_values = [ord(c) for c in chars]
    nth_smallest_ascii_value = sorted(ascii_values)[13]
    for c in chars:
        if ord(c) == nth_smallest_ascii_value:
            return c