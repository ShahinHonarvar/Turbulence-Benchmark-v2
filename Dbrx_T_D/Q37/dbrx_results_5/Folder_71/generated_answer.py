def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (ord('0') <= ord(char) <= ord('k') and 32 <= s.index(char) <= 46)]
    return ''.join(filtered_chars)