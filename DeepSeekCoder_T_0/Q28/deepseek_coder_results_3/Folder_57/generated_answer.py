def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[17:35]]
    chars.sort()
    return chr(chars[17])