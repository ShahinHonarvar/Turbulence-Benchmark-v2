def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(10, 83) if s[i].isascii()]
    ascii_vals = [ord(c) for c in chars]
    nth_smallest = ascii_vals[17]
    for c in chars:
        if ord(c) == nth_smallest:
            return c
    return None