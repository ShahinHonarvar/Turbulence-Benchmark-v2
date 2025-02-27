def return_nth_smallest_ascii(s):
    chars = sorted([ord(c) for c in s[1:67]])
    return chr(chars[7])