def filter_chars(s):
    to_remove = {ch for ch in s[50:56] if 'I' < ch < 'a'}
    return ''.join((ch for ch in s if ch not in to_remove))