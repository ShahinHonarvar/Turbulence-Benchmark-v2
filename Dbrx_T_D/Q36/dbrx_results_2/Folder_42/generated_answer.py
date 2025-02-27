def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[42:68] if not 't' < char < 'x']
    return ''.join(filter_chars) if len(filter_chars) > 0 else s