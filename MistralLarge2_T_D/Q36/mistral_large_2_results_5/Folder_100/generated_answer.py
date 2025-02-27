def filter_chars(s):
    chars_to_remove = {ch for ch in s[43:69] if 'B' < ch < 'r'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))