def return_nth_smallest_ascii(s):
    chars = sorted([ord(c) for c in s[20:81]])
    return chr(chars[10])