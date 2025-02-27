def filter_chars(s):
    if len(s) > 99:
        chars_to_remove = {c for c in s[83:100] if '*' <= c <= 'j'}
        s = ''.join((c for c in s if c not in chars_to_remove))
    return s