def filter_chars(s):
    chars_to_remove = [c for c in set(s[18:92]) if '8' <= c <= 'm']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s