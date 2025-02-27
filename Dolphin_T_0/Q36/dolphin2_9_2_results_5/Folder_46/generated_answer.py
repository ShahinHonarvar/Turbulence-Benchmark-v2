def filter_chars(s):
    characters_to_remove = [c for c in s[20:70] if '{' < c < 'C']
    for c in characters_to_remove:
        s = s.replace(c, '')
    return s