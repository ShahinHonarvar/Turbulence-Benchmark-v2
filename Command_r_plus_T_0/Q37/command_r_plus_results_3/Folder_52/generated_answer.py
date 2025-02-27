def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[54:84] if 'j' <= char <= 'v']
    return ''.join((char for char in s if char not in chars_to_remove))