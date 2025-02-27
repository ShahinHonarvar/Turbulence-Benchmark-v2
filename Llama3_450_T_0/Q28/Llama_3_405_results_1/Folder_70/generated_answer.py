def return_nth_smallest_ascii(s):
    chars = sorted(s[28:55])
    return sorted(chars, key=lambda x: ord(x))[13]