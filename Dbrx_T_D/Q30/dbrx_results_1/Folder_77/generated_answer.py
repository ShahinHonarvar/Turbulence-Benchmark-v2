def insert_before_character(s: str) -> str:
    return ''.join((c if c != '9' else 'h9' for c in s))