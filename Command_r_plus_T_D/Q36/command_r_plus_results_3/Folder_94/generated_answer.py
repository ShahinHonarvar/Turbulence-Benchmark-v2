def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 85 > ord(char) > ord('I')]
    return ''.join(filtered_chars)