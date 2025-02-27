def filter_chars(s):
    chars_to_remove = [c for c in s[138:921] if '6' <= c <= 'A']
    new_s = ''.join([c for c in s if c not in chars_to_remove])
    return new_s