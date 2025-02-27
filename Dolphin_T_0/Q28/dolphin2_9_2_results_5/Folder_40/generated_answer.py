def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[:5]]
    ascii_values.sort()
    return ascii_values[4]