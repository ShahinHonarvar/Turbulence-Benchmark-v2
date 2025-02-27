def insert_after_character(input_string: str) -> str:
    return ''.join((letter + 'F' if letter == 'U' else letter for letter in input_string))