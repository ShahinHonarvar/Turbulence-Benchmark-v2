def filter_chars(s):
    chars_to_remove = {ch for ch in s[70:97] if 'V' < ch < 'j'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))