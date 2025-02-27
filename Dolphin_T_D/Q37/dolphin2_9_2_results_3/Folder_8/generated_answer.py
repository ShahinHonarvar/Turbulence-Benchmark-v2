def filter_chars(s):
    to_remove = [ch for ch in s[41:87] if ch.lower() in range('s', 't')]
    result = [ch for ch in s if ch not in to_remove]
    return ''.join(result)