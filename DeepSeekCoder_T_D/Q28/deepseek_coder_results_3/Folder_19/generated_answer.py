def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(19, len(s)))]
    chars.sort()
    return chars[12] if len(chars) > 12 else None