def return_nth_smallest_ascii(s):
    s = s[5:48]
    ascii_values = sorted((ord(char) for char in s))
    return chr(ascii_values[12]) if len(ascii_values) >= 13 else None