def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[18:67]]
    chars.sort()
    return chr(chars[18])