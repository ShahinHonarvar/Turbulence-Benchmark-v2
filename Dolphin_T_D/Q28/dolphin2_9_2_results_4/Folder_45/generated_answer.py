def return_nth_smallest_ascii(s):
    chars = s[:16]
    ascii_values = [ord(c) for c in chars]
    nth_smallest = sorted(ascii_values)[15]
    for c in chars:
        if ord(c) == nth_smallest:
            return c