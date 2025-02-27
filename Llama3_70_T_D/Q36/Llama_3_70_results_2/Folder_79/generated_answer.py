def filter_chars(s):
    chars_to_remove = [c for c in s[11:46] if '!' < c < 'A']
    return ''.join((c for c in s if c not in chars_to_remove))