def return_nth_smallest_ascii(s):
    chars = sorted([ord(c) for c in s[5:48]])
    return chr(chars[12])