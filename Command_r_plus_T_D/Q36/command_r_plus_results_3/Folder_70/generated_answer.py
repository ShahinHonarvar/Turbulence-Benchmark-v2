def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(171, 195) if 33 < i < 123]
    return ''.join((char for char in s if char not in chars_to_remove))