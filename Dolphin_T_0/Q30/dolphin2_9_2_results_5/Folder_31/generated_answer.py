def insert_before_character(s: str) -> str:
    return 'N'.join(('B' if c == 'B' else c for c in s))