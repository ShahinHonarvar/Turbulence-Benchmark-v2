def return_nth_smallest_ascii(s):
    subset = s[34:82]
    ascii_values = sorted((ord(c) for c in subset if c != ' '))
    return chr(ascii_values[11]) if len(ascii_values) > 11 else None