def insert_after_character(input_string: str) -> str:
    return input_string.replace('s', 's' + 'w', 1) if input_string.count('s') else input_string