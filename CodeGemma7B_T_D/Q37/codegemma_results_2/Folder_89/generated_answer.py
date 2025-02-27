def filter_chars(text: str) -> str:
    """Filters characters between indices 11 and 32 (inclusive) that are greater than or equal to '!' and smaller than or equal to '@'."""
    return ''.join((char for char in text if not (11 <= text.index(char) <= 32 and char >= '!' and (char <= '@'))))