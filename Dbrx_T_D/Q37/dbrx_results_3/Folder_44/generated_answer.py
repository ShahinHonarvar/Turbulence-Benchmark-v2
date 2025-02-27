def filter_chars(s: str) -> str:
    filtered_chars = [char for i, char in enumerate(s) if i < 21 or i > 43 or ord(char) < ord('+') or (ord(char) > ord('8'))]
    return ''.join(filtered_chars)