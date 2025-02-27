def return_nth_smallest_ascii(s):
    chars = s[17:35]
    ascii_vals = [ord(c) for c in chars]
    nth_smallest = sorted(ascii_vals)[17]
    for c in chars:
        if ord(c) == nth_smallest:
            return c