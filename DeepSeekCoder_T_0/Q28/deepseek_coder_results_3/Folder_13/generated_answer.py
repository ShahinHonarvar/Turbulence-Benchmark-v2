def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[47:81]]
    chars.sort()
    return chr(chars[3]) if len(chars) > 3 else None