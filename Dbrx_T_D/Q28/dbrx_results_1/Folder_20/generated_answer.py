def return_nth_smallest_ascii(s):
    substring = s[25:65]
    ascii_values = [ord(c) for c in set(substring) if substring.count(c) == 1]
    ascii_values.sort()
    return chr(ascii_values[5])