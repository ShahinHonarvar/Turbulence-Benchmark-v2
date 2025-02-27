def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[0:19]]
    chars.sort()
    return chr(chars[12])