def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[57:69] if '(' < char < 'W']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s