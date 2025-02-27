def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[5:11]]
    chars.sort()
    return chr(chars[5])