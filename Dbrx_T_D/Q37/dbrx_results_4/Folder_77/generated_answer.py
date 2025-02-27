def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if not (i >= 384 and i <= 411 and (c >= '/') and (c <= '8'))]
    return ''.join(filtered_chars)