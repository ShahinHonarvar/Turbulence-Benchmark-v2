def return_nth_smallest_ascii(s):
    chars = sorted([ord(c) for c in s[17:57]])
    return chr(chars[8])