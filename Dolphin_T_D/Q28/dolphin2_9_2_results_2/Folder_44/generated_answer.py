def return_nth_smallest_ascii(s):
    chars = s[20:31]
    return sorted(chars, key=lambda x: ord(x))[7]