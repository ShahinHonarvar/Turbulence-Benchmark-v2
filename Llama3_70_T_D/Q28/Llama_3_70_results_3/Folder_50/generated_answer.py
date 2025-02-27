def return_nth_smallest_ascii(s):
    substring = s[25:89]
    ascii_values = [ord(c) for c in substring]
    sorted_ascii_values = sorted(set(ascii_values))
    nth_smallest_ascii = sorted_ascii_values[10]
    for char in substring:
        if ord(char) == nth_smallest_ascii:
            return char