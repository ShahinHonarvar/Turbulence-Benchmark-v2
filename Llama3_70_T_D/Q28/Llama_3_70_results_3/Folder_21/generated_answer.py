def return_nth_smallest_ascii(s):
    chars_in_range = sorted(s[8:66])
    ascii_values = [ord(c) for c in chars_in_range]
    sixth_smallest_ascii = sorted(set(ascii_values))[5]
    for c in chars_in_range:
        if ord(c) == sixth_smallest_ascii:
            return c