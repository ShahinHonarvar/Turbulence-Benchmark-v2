def filter_chars(s):
    if len(s) < 10:
        return s
    chars_to_remove = {ch for ch in s[2:9] if '8' < ch < 'm'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))