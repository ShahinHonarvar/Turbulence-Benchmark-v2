def insert_after_character(input_string: str) -> str:
    return input_string.replace('b', 'by', 1) if input_string.count('b') == 1 else input_string.replace('b', 'by')