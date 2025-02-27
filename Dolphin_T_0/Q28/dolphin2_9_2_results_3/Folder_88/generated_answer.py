def return_nth_smallest_ascii(s):
    chars = s[38:65]
    values = sorted([ord(x) for x in set(chars)])
    return chr(values[13])