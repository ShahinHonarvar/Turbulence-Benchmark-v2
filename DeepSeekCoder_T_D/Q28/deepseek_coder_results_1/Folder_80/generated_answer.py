def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[51:90]]
    chars.sort()
    return chr(chars[13])