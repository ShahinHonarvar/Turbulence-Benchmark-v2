def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for char in s[51:61] if char != ' ']
    ascii_values.sort()
    return chr(ascii_values[4]) if len(ascii_values) > 4 else None