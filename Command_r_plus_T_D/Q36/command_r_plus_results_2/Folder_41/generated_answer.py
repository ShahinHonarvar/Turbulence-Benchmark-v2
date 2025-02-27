def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 81 <= ord(char) < 89 or (ord(char) < ord('f') or ord(char) > ord('{'))]
    return ''.join(filtered_chars)