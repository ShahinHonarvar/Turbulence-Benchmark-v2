def return_nth_smallest_ascii(s):
    chars = list(s[:4])
    ascii_vals = [ord(c) for c in chars]
    nth_smallest_ascii = sorted(ascii_vals)[3]
    for c in chars:
        if ord(c) == nth_smallest_ascii:
            return c