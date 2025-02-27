def filter_chars(text: str) -> str:
    return ''.join((c for i, c in enumerate(text) if not (15 <= i <= 55 and c >= 'W' and (c <= '{'))))