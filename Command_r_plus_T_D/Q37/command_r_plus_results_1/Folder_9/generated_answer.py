def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i, char in enumerate(s[38:100], 38):
        if 'A' <= char <= 'Q':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))