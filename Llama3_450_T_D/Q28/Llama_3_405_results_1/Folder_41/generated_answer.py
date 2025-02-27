def return_nth_smallest_ascii(s):
    chars = sorted(s[58:86])
    return sorted(chars, key=lambda x: ord(x))[18]