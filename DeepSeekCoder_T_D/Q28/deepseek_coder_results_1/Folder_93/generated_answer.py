def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[42:60]]
    chars.sort()
    return chr(chars[16]) if len(chars) > 16 else None