def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[:4]]
    ascii_values.sort()
    return chr(ascii_values[3])