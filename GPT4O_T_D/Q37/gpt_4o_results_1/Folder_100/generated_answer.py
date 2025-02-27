def filter_chars(s):
    chars_to_remove = set(s[88:91])
    filtered_chars = {ch for ch in chars_to_remove if 'J' <= ch <= 'Q'}
    return ''.join((ch for ch in s if ch not in filtered_chars))