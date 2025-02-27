def filter_chars(s):
    chars_to_remove = [c for c in s[50:92] if 'A' < c < 'Q']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s