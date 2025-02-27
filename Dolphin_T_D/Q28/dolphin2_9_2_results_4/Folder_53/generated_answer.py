def return_nth_smallest_ascii(s):
    chars = s[40:61]
    return sorted(chars, key=lambda x: ord(x))[18]