def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[52:80]]
    chars.sort()
    return chr(chars[6])