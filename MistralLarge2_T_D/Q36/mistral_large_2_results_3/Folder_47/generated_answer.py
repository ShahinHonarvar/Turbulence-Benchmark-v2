def filter_chars(s):
    chars_to_remove = {ch for ch in s[45:57] if 'F' < ch < 'n'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))