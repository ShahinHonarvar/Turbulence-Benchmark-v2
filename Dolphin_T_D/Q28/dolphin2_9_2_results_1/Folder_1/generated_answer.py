def return_nth_smallest_ascii(s):
    substring = s[21:60]
    ascii_values = sorted(set((ord(c) for c in substring)))
    return chr(ascii_values[10])