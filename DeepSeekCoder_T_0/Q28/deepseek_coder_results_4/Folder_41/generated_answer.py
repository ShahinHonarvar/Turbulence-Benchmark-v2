def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[58:86]]
    chars.sort()
    return chr(chars[18]) if len(chars) > 18 else None