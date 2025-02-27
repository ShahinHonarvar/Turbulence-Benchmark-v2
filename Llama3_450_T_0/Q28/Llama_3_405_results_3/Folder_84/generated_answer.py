def return_nth_smallest_ascii(s):
    chars = sorted(s[52:80])
    return sorted(chars, key=lambda x: ord(x))[6]