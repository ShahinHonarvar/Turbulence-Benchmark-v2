def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(50, 76) if i < len(s)]
    chars.sort()
    return chars[6] if len(chars) > 6 else None