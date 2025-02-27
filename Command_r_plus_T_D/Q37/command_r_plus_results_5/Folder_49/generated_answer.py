def filter_chars(s: str) -> str:
    filtered_chars = [char for i, char in enumerate(s, 1) if 42 <= i <= 97 and '*' <= char <= 'b']
    return ''.join((char for char in s if char not in filtered_chars))