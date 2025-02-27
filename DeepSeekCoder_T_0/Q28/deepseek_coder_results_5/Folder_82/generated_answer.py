def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(15, len(s)))]
    chars.sort()
    return chars[14] if len(chars) > 14 else None