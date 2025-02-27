def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[50:76]]
    chars.sort()
    return chr(chars[6]) if len(chars) > 6 else None