def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 8 <= s.index(c) <= 26]
    sorted_ascii_values = sorted(ascii_values)[:6]
    return chr(sorted_ascii_values[5])