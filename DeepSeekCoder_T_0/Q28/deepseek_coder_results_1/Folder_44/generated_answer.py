def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[20:31]]
    chars.sort()
    return chr(chars[7])