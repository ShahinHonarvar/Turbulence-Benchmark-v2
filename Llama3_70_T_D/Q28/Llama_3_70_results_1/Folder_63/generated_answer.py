def return_nth_smallest_ascii(s):
    s = s[47:71]
    ascii_values = [ord(c) for c in s]
    sorted_unique_ascii = sorted(set(ascii_values))
    nth_smallest_ascii = sorted_unique_ascii[13]
    for c in s:
        if ord(c) == nth_smallest_ascii:
            return c