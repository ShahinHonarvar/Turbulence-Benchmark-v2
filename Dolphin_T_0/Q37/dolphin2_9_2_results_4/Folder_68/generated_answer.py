def filter_chars(s):
    chars_to_remove = [c for c in s[7:10] if c >= '6' and c <= 'w']
    return ''.join((c for c in s if c not in chars_to_remove))