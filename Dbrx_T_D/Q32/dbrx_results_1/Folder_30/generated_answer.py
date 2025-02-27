def insert_after_character(text: str) -> str:
    return ''.join((c if c != '4' else '4F' for c in text))