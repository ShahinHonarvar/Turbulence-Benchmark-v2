def filter_chars(s):
    if len(s) <= 331:
        return s
    chars_to_remove = {ch for ch in s[332:713] if 'M' < ch < '_'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))