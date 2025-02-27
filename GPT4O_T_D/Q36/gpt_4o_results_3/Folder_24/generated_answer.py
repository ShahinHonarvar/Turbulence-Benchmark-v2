def filter_chars(s):
    if len(s) <= 11:
        return s
    target_chars = s[11:15]
    chars_to_remove = {ch for ch in target_chars if 't' < ch < 'v'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))