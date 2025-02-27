def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(17, len(s)))]
    chars.sort()
    return chars[16] if len(chars) > 16 else None