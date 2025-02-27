def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(34, 37) if chr(i) > '>' and chr(i) < 'A']
    return ''.join([c for c in s if c not in chars_to_remove])