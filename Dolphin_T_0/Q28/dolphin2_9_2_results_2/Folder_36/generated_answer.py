def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[17:57] if c not in s[:17] and c not in s[57:]]
    return chr(sorted(ascii_values)[8])