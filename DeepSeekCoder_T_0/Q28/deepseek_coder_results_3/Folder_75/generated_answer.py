def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[62:84]]
    chars.sort()
    return chr(chars[8]) if len(chars) > 8 else None