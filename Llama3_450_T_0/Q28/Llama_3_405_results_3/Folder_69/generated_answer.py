def return_nth_smallest_ascii(s):
    chars = sorted(s[67:78])
    return sorted(chars, key=lambda x: ord(x))[6]