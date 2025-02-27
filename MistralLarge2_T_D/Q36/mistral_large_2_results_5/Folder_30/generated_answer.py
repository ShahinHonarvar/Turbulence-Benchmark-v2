def filter_chars(s):
    chars_to_remove = {ch for ch in s[23:45] if '3' < ch < 'I'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))