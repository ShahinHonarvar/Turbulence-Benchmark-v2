def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[227:236] if 'D' <= char <= 'u']
    return ''.join((char for char in s if char not in chars_to_remove))