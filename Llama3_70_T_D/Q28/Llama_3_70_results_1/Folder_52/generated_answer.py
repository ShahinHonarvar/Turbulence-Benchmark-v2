def return_nth_smallest_ascii(s):
    substring = s[46:73]
    ascii_values = [ord(c) for c in substring]
    sorted_ascii_values = sorted(set(ascii_values))
    nth_smallest = sorted_ascii_values[14]
    for c in substring:
        if ord(c) == nth_smallest:
            return c