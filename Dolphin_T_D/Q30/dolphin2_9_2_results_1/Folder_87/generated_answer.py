def insert_before_character(string: str) -> str:
    new_string = ''
    for char in string:
        if char == 'm':
            new_string += 'N' + char
        else:
            new_string += char
    return new_string