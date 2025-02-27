def filter_chars(s):
    if len(s) >= 4:
        to_remove = [c for c in s[2:4] if '5' <= c <= '_']
        for char in to_remove:
            s = s.replace(char, '')
    return s