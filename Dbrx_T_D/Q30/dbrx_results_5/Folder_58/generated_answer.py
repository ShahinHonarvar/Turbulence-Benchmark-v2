def insert_before_character(input_string: str) -> str:
    return ''.join(['o' if char == 'F' else char for char in input_string])