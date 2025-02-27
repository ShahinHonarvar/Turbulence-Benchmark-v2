def filter_chars(s):
    s = list(s)
    chars_to_remove = [c for c in s[31:73] if 'M' < c < 'j']
    for c in chars_to_remove:
        s = [x for x in s if x != c]
    return ''.join(s)