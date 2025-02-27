def filter_chars(s: str) -> str:
    start, end = (43, 83)
    filtered_chars = [char for i, char in enumerate(s) if not (start < i < end and ':' > char > 'Q')]
    return ''.join(filtered_chars)