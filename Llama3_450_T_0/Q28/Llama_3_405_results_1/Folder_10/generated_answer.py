def return_nth_smallest_ascii(s):
    chars = sorted(s[38:83])
    return sorted(chars, key=lambda x: ord(x))[19]