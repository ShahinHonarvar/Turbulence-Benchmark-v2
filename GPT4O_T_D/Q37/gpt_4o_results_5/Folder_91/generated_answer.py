def filter_chars(s):
    if len(s) > 8:
        target_chars = s[7:9]
        remove_chars = {ch for ch in target_chars if 'B' <= ch <= 'H'}
        result = ''.join((ch for ch in s if ch not in remove_chars))
        return result
    return s