def return_nth_smallest_ascii(s):
    s = s[:7]
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[6]
    for char in s:
        if ord(char) == nth_smallest_ascii:
            return char