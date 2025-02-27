def filter_chars(s):
    if len(s) <= 77:
        return s
    chars_to_remove = {ch for ch in s[78:87] if ';' < ch < 'r'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))