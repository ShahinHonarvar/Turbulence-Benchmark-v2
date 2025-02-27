def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[1:7] if '3' < char < '^']
    return ''.join((char for char in s if char not in chars_to_remove))