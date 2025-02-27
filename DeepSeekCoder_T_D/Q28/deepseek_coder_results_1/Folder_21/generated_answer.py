def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[8:66]]
    chars.sort()
    return chr(chars[5])