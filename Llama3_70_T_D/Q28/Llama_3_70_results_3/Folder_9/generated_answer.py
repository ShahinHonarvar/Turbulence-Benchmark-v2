def return_nth_smallest_ascii(s):
    s = s[10:91]
    ascii_values = [ord(c) for c in s]
    ascii_values.sort()
    return chr(ascii_values[19])