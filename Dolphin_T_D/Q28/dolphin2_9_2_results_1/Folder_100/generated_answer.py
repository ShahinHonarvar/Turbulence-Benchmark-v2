def return_nth_smallest_ascii(s):
    chars = list(s[5:48])
    return sorted(chars, key=lambda c: ord(c))[12]