def filter_chars(s):
    if len(s) <= 58:
        return s
    chars_to_remove = {ch for ch in s[59:81] if '5' < ch < '>'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))