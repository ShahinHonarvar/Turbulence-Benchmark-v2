def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(12, len(s)))]
    chars.sort()
    return chars[11] if len(chars) > 11 else None