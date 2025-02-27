def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[:6]]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[5])