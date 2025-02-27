def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if s.index(char) < 75 or s.index(char) > 99 or ord('8') > ord(char) > ord('e')]
    return ''.join(filtered_chars)