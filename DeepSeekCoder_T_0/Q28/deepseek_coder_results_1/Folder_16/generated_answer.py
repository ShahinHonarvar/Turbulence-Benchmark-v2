def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[18:46]]
    chars.sort()
    return chr(chars[6])