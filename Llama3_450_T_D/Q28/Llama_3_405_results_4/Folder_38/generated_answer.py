def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:46])
    ascii_values = [ord(c) for c in sorted_chars]
    ascii_values.sort()
    return chr(ascii_values[9])