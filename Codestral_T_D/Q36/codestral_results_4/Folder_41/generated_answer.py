def filter_chars(s):
    chars_to_remove = [ch for ch in s[81:89] if 'f' < ch < '{']
    return ''.join([ch for ch in s if ch not in chars_to_remove])