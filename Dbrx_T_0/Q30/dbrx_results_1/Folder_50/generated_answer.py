def insert_before_character(input_string: str) -> str:
    return input_string.replace('t', 'ut', 1) if input_string[0] == 't' else 'u' + input_string.replace('t', 'ut')