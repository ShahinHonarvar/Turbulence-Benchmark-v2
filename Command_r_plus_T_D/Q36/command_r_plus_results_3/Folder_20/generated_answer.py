def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 60 < ord(char) < 67]
    return ''.join(filtered_chars)