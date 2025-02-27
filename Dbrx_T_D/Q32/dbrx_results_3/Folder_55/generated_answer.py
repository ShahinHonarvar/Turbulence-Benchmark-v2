def insert_after_character(input_string: str) -> str:
    return input_string.replace('u', 'uU', 1) if input_string.count('u') else input_string