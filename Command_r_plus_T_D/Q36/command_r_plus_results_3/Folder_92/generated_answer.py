def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if char <= ',' or char >= 'f']
    return ''.join(filtered_chars)