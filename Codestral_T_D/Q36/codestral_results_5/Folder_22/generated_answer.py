def filter_chars(s):
    chars_to_remove = [ch for ch in s[55:84] if ';' < ch < 'z']
    return ''.join((ch for ch in s if ch not in chars_to_remove))