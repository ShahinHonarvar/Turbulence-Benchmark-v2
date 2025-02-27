def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(9, len(s)))]
    chars.sort()
    return chars[8] if len(chars) > 8 else None