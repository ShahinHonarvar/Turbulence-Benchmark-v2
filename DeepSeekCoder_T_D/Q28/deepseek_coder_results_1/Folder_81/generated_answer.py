def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(14, len(s)))]
    chars.sort()
    return chars[13] if len(chars) > 13 else None