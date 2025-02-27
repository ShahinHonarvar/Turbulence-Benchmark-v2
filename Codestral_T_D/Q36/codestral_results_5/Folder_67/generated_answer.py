def filter_chars(s):
    chars_to_remove = [c for c in s[18:31] if 'H' < c < '|']
    return ''.join([ch for ch in s if ch not in chars_to_remove])