def insert_after_character(input_string: str) -> str:
    return input_string.replace('i', 'iI').replace('I', 'Ii', 1)