def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[51:61]]
    chars.sort()
    return chr(chars[4])