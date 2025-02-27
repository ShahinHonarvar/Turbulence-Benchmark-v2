def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[17:87]]
    chars.sort()
    return chr(chars[14]) if len(chars) > 14 else None