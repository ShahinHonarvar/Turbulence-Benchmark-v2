def insert_before_character(input_string: str) -> str:
    return input_string.replace('i', 'Ii') if 'i' in input_string else input_string