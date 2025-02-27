def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[14:36]]
    chars.sort()
    return chr(chars[10]) if len(chars) > 10 else None