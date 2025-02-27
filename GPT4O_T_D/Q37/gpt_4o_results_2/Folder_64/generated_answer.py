def filter_chars(s):
    chars_to_remove = {c for c in s[1:8] if 'L' <= c <= 'a'}
    return ''.join((c for c in s if c not in chars_to_remove))