def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(18, len(s)))]
    chars.sort()
    return chars[17] if len(chars) > 17 else None