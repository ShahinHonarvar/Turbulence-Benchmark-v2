def insert_before_character(s: str) -> str:
    return 's'.join(('H' if c == 'H' else c for c in s))