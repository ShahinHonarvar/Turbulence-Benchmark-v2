def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s[46:73]]
    ascii_chars.sort()
    return chr(ascii_chars[14])