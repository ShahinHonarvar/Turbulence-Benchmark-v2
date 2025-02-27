def filter_chars(s: str) -> str:
    filtered_chars = [char for i, char in enumerate(s) if not (23 < i < 83 and ord('f') < ord(char) < ord('o'))]
    return ''.join(filtered_chars)