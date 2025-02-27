def insert_after_character(input_string: str) -> str:
    return input_string.replace('g', 'gM', 1) if 'g' in input_string else input_string