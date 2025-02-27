def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[36:41] if 'H' <= char <= 'e']
    return ''.join((char for char in s if char not in chars_to_remove))