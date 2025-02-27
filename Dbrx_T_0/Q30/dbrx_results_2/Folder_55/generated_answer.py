def insert_before_character(input_string: str) -> str:
    return input_string.replace('u', 'Uu') if 'u' in input_string else input_string