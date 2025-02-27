def filter_chars(s):
    chars_to_remove = {ch for ch in s[19:64] if '3' < ch < 'B'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))