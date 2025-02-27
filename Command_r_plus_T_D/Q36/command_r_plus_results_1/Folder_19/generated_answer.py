def filter_chars(s: str) -> str:
    filter_range = range(77, 88)
    filtered_chars = [c for i, c in enumerate(s) if i not in filter_range or (ord(c) <= ord(';') or ord(c) >= ord('r'))]
    return ''.join(filtered_chars)