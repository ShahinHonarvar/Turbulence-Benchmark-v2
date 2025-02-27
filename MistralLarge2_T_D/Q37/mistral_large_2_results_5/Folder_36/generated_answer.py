def filter_chars(s):
    to_remove = {ch for i, ch in enumerate(s) if 259 <= i <= 502 and ',' <= ch <= '3'}
    return ''.join((ch for ch in s if ch not in to_remove))