def return_nth_smallest_ascii(s):
    s = s[25:89]
    ascii_values = sorted([ord(c) for c in s])
    unique_ascii_values = []
    for i in ascii_values:
        if i not in unique_ascii_values:
            unique_ascii_values.append(i)
    nth_smallest_ascii = unique_ascii_values[10]
    for c in s:
        if ord(c) == nth_smallest_ascii:
            return c