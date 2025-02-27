def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[12:88]]
    chars.sort()
    return chr(chars[16])