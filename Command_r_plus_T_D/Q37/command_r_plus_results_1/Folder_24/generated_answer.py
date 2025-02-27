def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (36 <= ord(char) <= 79 and '2' <= char <= 's')]
    return ''.join(filtered_chars)