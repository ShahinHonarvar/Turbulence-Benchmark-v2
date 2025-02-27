def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(16, len(s)))]
    chars.sort()
    return chars[15] if len(chars) > 15 else None