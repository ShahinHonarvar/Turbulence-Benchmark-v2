def return_nth_smallest_ascii(s):
    chars = sorted(s[60:84])
    return sorted(chars, key=lambda x: ord(x))[13]