def return_nth_smallest_ascii(s):
    chars = s[14:67]
    return sorted(chars, key=lambda c: ord(c))[7]