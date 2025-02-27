def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 83 <= ord(char) <= 99 or not ord('*') <= ord(char) <= ord('j')]
    return ''.join(filtered_chars)