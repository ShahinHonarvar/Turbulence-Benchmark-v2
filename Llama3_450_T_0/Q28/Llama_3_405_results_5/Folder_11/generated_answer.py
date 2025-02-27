def return_nth_smallest_ascii(s):
    chars = sorted(s[9:60])
    return sorted(chars, key=lambda x: ord(x))[5]