def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[602:760] if 'Q' <= char <= 'h']
    return ''.join((char for char in s if char not in chars_to_remove))