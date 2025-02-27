def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (227 <= ord(char) <= 235 and 'D' <= char <= 'u')]
    return ''.join(filtered_chars)