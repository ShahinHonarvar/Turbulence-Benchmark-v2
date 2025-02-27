def insert_after_character(input_string: str) -> str:
    return input_string.replace('t', 'tu', 1) if input_string.startswith('t') else 'u' + input_string.replace('t', 'tu', 1)