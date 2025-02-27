def filter_chars(s: str) -> str:
    filter_range = set(range(ord('5'), ord('_') + 1))
    chars_to_remove = {char for char in s[2:4] if ord(char) in filter_range}
    return ''.join((char for char in s if char not in chars_to_remove))