def filter_chars(s):
    if len(s) <= 299:
        return s
    segment = s[300:418]
    to_remove = {ch for ch in segment if '9' < ch < 'P'}
    return ''.join((ch for ch in s if ch not in to_remove))