def filter_chars(s):
    if len(s) <= 44:
        return s
    to_remove = [ch for ch in s[44:59] if '5' < ch < 'C']
    return ''.join((ch for ch in s if ch not in to_remove))