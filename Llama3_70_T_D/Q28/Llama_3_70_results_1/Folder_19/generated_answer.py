def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[:19]]
    sorted_ascii = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii[12]
    for c in s[:19]:
        if ord(c) == nth_smallest_ascii:
            return c