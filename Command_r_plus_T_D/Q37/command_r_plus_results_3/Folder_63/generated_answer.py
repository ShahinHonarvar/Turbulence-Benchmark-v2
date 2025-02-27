def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[42:93] if '/' <= char <= 'a']
    return ''.join((char for char in s if char not in chars_to_remove))