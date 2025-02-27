def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(s[i]) for i in range(min(len(s), 5))))
    return chr(ascii_values[4]) if len(ascii_values) > 4 else None