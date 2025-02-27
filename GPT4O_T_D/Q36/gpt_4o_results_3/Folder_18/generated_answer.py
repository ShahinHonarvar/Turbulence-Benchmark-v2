def filter_chars(s):
    if len(s) > 648:
        chars_to_remove = {ch for ch in s[588:648] if ',' < ch < 'c'}
        s = ''.join((ch for ch in s if ch not in chars_to_remove))
    return s