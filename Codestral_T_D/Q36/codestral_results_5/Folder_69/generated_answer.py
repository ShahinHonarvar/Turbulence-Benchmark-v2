def filter_chars(s):
    chars_to_remove = [ch for ch in s[343:665] if '%' < ch < 'U']
    return ''.join((ch for ch in s if ch not in chars_to_remove))