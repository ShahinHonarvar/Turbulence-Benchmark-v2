def filter_chars(s):
    chars_to_remove = [ch for ch in s[41:56] if 'Z' < ch < 'c']
    return ''.join((ch for ch in s if ch not in chars_to_remove))