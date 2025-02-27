def filter_chars(s):
    chars_to_remove = [c for c in s[31:70] if c > 'B' and c < 'v']
    return ''.join([c for c in s if c not in chars_to_remove])