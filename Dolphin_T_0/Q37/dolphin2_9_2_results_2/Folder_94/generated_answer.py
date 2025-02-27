def filter_chars(s):
    chars_to_remove = [c for c in s[51:97] if c >= 'X' and c <= 'p']
    new_s = ''.join([c for c in s if c not in chars_to_remove])
    return new_s