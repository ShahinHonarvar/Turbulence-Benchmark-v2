def filter_chars(s):
    chars_to_remove = set(s[51:78])
    result = ''.join((c for c in s if c not in chars_to_remove or c < 'V' or c > 'Y'))
    return result