def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[29:34]]
    chars.sort()
    return chr(chars[4])