def filter_chars(s: str) -> str:
    chars_to_remove = set('@ABCDEFGHIJKLMNo')
    return ''.join((char for char in s if char not in chars_to_remove))