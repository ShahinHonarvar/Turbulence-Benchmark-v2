def return_nth_smallest_ascii(s):
    ascii_values = [ord(ch) for ch in s[:5]]
    ascii_values.sort()
    return chr(ascii_values[4])