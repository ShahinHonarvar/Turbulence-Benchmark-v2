def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 82 < s.index(char) < 89 or not (ord(char) > ord('*') and ord(char) < ord('['))]
    return ''.join(filtered_chars)