def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[602:760] if 'Q' <= char <= 'h']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s