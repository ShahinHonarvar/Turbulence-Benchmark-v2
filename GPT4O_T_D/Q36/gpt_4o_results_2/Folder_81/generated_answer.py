def filter_chars(s):
    if len(s) <= 76:
        return s
    chars_to_remove = {ch for ch in s[52:76] if '5' < ch < 'f'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))