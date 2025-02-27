def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[379:899] if 'M' <= char <= 'v']
    return ''.join((char for char in s if char not in chars_to_remove))