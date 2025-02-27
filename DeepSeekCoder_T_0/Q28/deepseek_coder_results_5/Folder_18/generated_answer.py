def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(51, 61) if i < len(s)]
    if len(chars) < 5:
        return None
    chars.sort()
    return chars[4] if len(chars) > 4 else None