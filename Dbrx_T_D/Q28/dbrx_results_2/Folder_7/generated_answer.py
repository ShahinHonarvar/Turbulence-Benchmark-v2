def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(s[i]) for i in range(12, 56) if 12 <= i <= 55))
    return chr(ascii_values[16]) if len(ascii_values) > 16 else None