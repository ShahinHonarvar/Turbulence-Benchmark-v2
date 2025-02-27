def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[70:75] if 'A' < char < 'U']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s