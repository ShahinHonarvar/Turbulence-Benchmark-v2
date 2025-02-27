def filter_chars(s):
    to_remove = [ch for ch in s[669:888] if 'B' < ch < 'Y']
    s = ''.join((ch for ch in s if ch not in to_remove))
    return s