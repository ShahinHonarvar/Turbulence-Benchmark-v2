def return_nth_smallest_ascii(s):
    chars = sorted(s[18:46])
    return sorted(chars, key=lambda x: ord(x))[6]