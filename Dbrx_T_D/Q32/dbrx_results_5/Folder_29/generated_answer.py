def insert_after_character(s: str) -> str:
    return ''.join((c if c != 'N' else 'Nz' for c in s))