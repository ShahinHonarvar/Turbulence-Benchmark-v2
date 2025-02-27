def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(27, 86) if chr(i) >= '!' and chr(i) <= 'B'}
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result