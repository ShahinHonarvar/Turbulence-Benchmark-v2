def filter_chars(s: str) -> str:
    start, end = (10, 15)
    filtered_chars = [c for c in s if c < 't' or c > 'v']
    return ''.join(filtered_chars[:start] + filtered_chars[end:])