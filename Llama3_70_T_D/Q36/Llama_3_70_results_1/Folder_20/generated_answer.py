def filter_chars(s):
    s = list(s)
    chars_to_remove = [c for c in s[13:40] if ':' < c < 'C']
    for c in chars_to_remove:
        s = [x for x in s if x != c]
    return ''.join(s)