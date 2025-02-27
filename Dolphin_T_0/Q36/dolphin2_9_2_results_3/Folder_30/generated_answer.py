def filter_chars(s):
    chars_to_remove = [c for c in s[23:45] if c > '3' and c < 'I']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s