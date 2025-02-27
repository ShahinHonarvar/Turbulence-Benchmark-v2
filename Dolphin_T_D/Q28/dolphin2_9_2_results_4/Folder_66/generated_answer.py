def return_nth_smallest_ascii(s):
    chars = s[35:53]
    return sorted(chars, key=lambda c: ord(c))[9]