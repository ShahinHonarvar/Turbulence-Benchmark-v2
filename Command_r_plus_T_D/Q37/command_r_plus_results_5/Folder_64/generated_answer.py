def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 'L' <= char <= 'a' or char not in s[1:8]]
    return ''.join(filtered_chars)