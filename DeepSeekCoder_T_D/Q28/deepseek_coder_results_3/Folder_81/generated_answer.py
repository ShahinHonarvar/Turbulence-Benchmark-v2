def return_nth_smallest_ascii(s):
    chars = [ord(s[i]) for i in range(min(14, len(s)))]
    chars.sort()
    return chr(chars[13]) if len(chars) > 13 else None