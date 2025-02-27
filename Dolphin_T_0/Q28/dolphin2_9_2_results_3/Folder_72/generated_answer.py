def return_nth_smallest_ascii(s):
    chars = s[33:61]
    return sorted(chars, key=lambda c: ord(c))[17]