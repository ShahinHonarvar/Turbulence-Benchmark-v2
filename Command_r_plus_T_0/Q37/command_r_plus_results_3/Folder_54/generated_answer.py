def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 46 or i > 85 or (ord(c) < 45 or ord(c) > 88)))
    return filtered_string