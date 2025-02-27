def filter_chars(s):
    to_remove = {ch for ch in s[59:81] if '5' < ch < '>'}
    return ''.join((ch for ch in s if ch not in to_remove))