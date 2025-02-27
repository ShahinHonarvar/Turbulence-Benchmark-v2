def return_nth_smallest_ascii(s):
    chars = s[14:36]
    return sorted(chars, key=lambda c: ord(c))[9]