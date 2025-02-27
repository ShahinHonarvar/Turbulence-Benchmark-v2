def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[259:503] if char >= ',' and char <= '3']
    return ''.join((char for char in s if char not in chars_to_remove))