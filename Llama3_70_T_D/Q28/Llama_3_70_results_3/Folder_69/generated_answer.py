def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(67, 78)]
    ascii_values = sorted([ord(c) for c in chars])
    nth_smallest_ascii = ascii_values[6]
    for char in chars:
        if ord(char) == nth_smallest_ascii:
            return char