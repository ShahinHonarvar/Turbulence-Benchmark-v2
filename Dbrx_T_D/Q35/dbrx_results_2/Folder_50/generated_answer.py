def remove_repeat_chars(s):
    chars = s[13:76]
    unique_chars = [c for i, c in enumerate(chars) if chars[:i].count(c) == 0]
    return s[:13] + ''.join(unique_chars) + s[76:]