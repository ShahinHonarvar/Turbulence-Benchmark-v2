def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 35:
        chars_to_remove.update({ch for ch in s[35:99] if 'A' <= ch <= 'b'})
    return ''.join((ch for ch in s if ch not in chars_to_remove))