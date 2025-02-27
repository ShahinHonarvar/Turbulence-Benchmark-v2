def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[477:985] if ',' <= char <= 'V']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s