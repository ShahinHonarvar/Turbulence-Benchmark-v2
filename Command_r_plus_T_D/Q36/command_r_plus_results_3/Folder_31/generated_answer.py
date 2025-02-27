def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[14:75] if '9' < char < 'K']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s