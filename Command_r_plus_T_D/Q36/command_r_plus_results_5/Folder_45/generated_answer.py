def filter_chars(s: str) -> str:
    filter_range = range(81, 86)
    chars_to_remove = [char for char in s[81:86] if '!' < char < 's']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s