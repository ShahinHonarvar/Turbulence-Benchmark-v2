def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[8:27]]
    chars.sort()
    return chr(chars[5]) if len(chars) > 5 else None