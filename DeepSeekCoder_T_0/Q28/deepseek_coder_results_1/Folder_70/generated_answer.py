def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[28:55]]
    chars.sort()
    return chr(chars[13]) if len(chars) > 13 else None