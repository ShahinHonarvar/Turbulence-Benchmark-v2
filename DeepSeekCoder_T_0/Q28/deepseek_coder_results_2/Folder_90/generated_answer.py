def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[17:84]]
    chars.sort()
    return chr(chars[4]) if len(chars) > 4 else None