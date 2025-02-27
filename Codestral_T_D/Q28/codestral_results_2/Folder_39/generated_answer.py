def return_nth_smallest_ascii(s):
    s = s[1:67]
    ascii_values = sorted(set((ord(c) for c in s)))
    return chr(ascii_values[7])