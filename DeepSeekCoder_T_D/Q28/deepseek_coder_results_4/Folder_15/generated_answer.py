def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(6) if i < len(s)]
    chars.sort()
    return chars[5] if len(chars) > 5 else None