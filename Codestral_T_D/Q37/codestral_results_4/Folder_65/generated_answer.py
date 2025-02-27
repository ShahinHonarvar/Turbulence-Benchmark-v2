def filter_chars(s):
    chars_to_remove = [ch for ch in s[61:71] if '0' <= ch <= '@']
    return ''.join((ch for ch in s if ch not in chars_to_remove))