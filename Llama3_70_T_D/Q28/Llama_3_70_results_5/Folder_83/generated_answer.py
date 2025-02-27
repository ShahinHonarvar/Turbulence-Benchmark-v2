def return_nth_smallest_ascii(s):
    s = s[30:71]
    ascii_values = [ord(c) for c in s]
    unique_ascii_values = sorted(list(set(ascii_values)))
    nth_smallest_ascii = unique_ascii_values[14]
    for c in s:
        if ord(c) == nth_smallest_ascii:
            return c