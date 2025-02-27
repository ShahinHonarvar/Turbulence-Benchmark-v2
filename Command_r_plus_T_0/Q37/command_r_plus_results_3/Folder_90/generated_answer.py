def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[347:853] if 'J' <= char <= 'b']
    return ''.join((char for char in s if char not in chars_to_remove))