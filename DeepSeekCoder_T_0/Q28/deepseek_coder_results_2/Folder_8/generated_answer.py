def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[60:89]]
    chars.sort()
    return chr(chars[6])